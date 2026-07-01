import os
import re
from src.parser.chatgpt_parser import cargar_conversaciones, extraer_mensajes, resumir_conversacion

CARPETA_DATOS = "data"
CARPETA_VAULT = "vault/conversaciones"


def limpiar_nombre_archivo(texto):
    """Convierte un titulo en un nombre de archivo seguro para el sistema operativo."""
    texto = texto.strip()
    texto = re.sub(r'[\\/*?:"<>|]', "", texto)
    texto = texto[:80]
    return texto if texto else "Sin titulo"


def conversacion_a_markdown(conversacion):
    """Convierte una conversacion completa en texto Markdown para Obsidian."""
    resumen = resumir_conversacion(conversacion)
    mensajes = extraer_mensajes(conversacion)

    lineas = []
    lineas.append("---")
    lineas.append(f"titulo: \"{resumen['titulo']}\"")
    lineas.append(f"fecha: {resumen['fecha']}")
    lineas.append(f"mensajes: {resumen['cantidad_mensajes']}")
    lineas.append("origen: ChatGPT")
    lineas.append("---")
    lineas.append("")
    lineas.append(f"# {resumen['titulo']}")
    lineas.append("")

    for m in mensajes:
        autor = "🧑 Usuario" if m["autor"] == "user" else "🤖 Asistente"
        lineas.append(f"### {autor}")
        lineas.append("")
        lineas.append(m["texto"])
        lineas.append("")

    return "\n".join(lineas)


def exportar_archivo(nombre_archivo):
    conversaciones = cargar_conversaciones(nombre_archivo)
    os.makedirs(CARPETA_VAULT, exist_ok=True)
    contador = 0

    for conv in conversaciones:
        resumen = resumir_conversacion(conv)
        nombre_seguro = limpiar_nombre_archivo(resumen["titulo"])
        ruta_nota = os.path.join(CARPETA_VAULT, f"{resumen['fecha']} - {nombre_seguro}.md")

        contenido = conversacion_a_markdown(conv)
        with open(ruta_nota, "w", encoding="utf-8") as f:
            f.write(contenido)
        contador += 1

    return contador


if __name__ == "__main__":
    total = exportar_archivo("conversations-000.json")
    print(f"Se crearon {total} notas en {CARPETA_VAULT}")
