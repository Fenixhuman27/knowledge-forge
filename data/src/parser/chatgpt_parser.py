import json
import os
from datetime import datetime

CARPETA_DATOS = "data"


def cargar_conversaciones(nombre_archivo):
    """Carga y devuelve la lista de conversaciones de un archivo JSON."""
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def extraer_mensajes(conversacion):
    """Recorre el 'mapping' de una conversacion y devuelve una lista
    de mensajes ordenados con su autor y texto."""
    mapping = conversacion.get("mapping", {})
    mensajes = []

    for nodo_id, nodo in mapping.items():
        mensaje = nodo.get("message")
        if mensaje is None:
            continue

        autor = mensaje.get("author", {}).get("role", "desconocido")
        contenido = mensaje.get("content", {})
        partes = contenido.get("parts", [])

        texto = " ".join(p for p in partes if isinstance(p, str)).strip()

        if texto:
            mensajes.append({
                "autor": autor,
                "texto": texto,
                "create_time": mensaje.get("create_time"),
            })

    mensajes.sort(key=lambda m: (m["create_time"] is None, m["create_time"]))
    return mensajes


def resumir_conversacion(conversacion):
    """Devuelve un resumen simple de una conversacion: titulo, fecha y cantidad de mensajes."""
    titulo = conversacion.get("title") or "Sin titulo"
    create_time = conversacion.get("create_time")
    fecha = datetime.fromtimestamp(create_time).strftime("%Y-%m-%d") if create_time else "Sin fecha"
    mensajes = extraer_mensajes(conversacion)

    return {
        "titulo": titulo,
        "fecha": fecha,
        "cantidad_mensajes": len(mensajes),
    }


if __name__ == "__main__":
    conversaciones = cargar_conversaciones("conversations-000.json")
    print(f"Se encontraron {len(conversaciones)} conversaciones en el archivo")

    for conv in conversaciones[:5]:
        resumen = resumir_conversacion(conv)
        print(f"- [{resumen['fecha']}] {resumen['titulo']} ({resumen['cantidad_mensajes']} mensajes)")