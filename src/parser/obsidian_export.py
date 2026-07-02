import os
import re
from src.parser.chatgpt_parser import cargar_conversaciones, extraer_mensajes, resumir_conversacion
from src.parser.temas import detectar_temas

CARPETA_DATOS = "data"
CARPETA_VAULT = "vault/conversaciones"


def limpiar_nombre_archivo(texto):
    texto = texto.strip()
    texto = re.sub(r'[\\/*?:"<>|]', "", texto)
    texto = texto[:80]
    return texto if texto else "Sin titulo"


def conversacion_a_markdown(conversacion):
    resumen = resumir_conversacion(conversacion)
    mensajes = extraer_mensajes(conversacion)
    temas = detectar_temas(resumen["titulo"])

    lineas = []
    lineas.append("---")
    lineas.append(f"titulo: \"{resumen['titulo']}\"")
    lineas.append(f"fecha: {resumen['fecha']}")
    lineas.append(f"mensajes: {resumen['cantidad_mensajes']}")
    lineas.append("origen: ChatGPT")
    if temas:
        lineas.append("tags:")
        for tema in temas:
            lineas.append(f"  - {tema}")
    lineas.append("---")
    lineas.append("")
    lineas.append(f"# {resumen['titulo']}")
    lineas.append("")

    if temas:
        lineas.append("Temas: " + ", ".join(f"#{t}" for t in temas))
        lineas.append("")

    for m in mensajes:
        autor = "Usuario" if m["autor"] == "user" else "Asistente"
        lineas.append(f"### {autor}")
        lineas.append("")
        lineas.append(m["texto"])
        lineas.append("")

    return "\n".join(lineas)


def nombre_archivo_unico(conversacion, resumen):
    nombre_seguro = limpiar_nombre_archivo(resumen["titulo"])
    id_corto = conversacion.get("conversation_id", "")[:8]
    return f"{resumen['fecha']} - {nombre_seguro} - {id_corto}.md"


def exportar_archivo(nombre_archivo):
    conversaciones = cargar_conversaciones(nombre_archivo)
    os.makedirs(CARPETA_VAULT, exist_ok=True)
    contador = 0

    for conv in conversaciones:
        resumen = resumir_conversacion(conv)
        nombre = nombre_archivo_unico(conv, resumen)
        ruta_nota = os.path.join(CARPETA_VAULT, nombre)

        contenido = conversacion_a_markdown(conv)
        with open(ruta_nota, "w", encoding="utf-8") as f:
            f.write(contenido)
        contador += 1

    return contador


if __name__ == "__main__":
    total = exportar_archivo("conversations-000.json")
    print(f"Se crearon {total} notas en {CARPETA_VAULT}")
