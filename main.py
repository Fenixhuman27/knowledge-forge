import os
from src.parser.chatgpt_parser import cargar_conversaciones, resumir_conversacion

CARPETA_DATOS = "data"


def buscar_archivos_conversaciones():
    """Busca archivos JSON que contienen conversaciones (empiezan con 'conversations')."""
    archivos = [
        f for f in os.listdir(CARPETA_DATOS)
        if f.startswith("conversations") and f.endswith(".json")
    ]
    return sorted(archivos)


def procesar_todo():
    archivos = buscar_archivos_conversaciones()
    total_conversaciones = 0

    for archivo in archivos:
        conversaciones = cargar_conversaciones(archivo)
        print(f"\n=== {archivo} ({len(conversaciones)} conversaciones) ===")

        for conv in conversaciones:
            resumen = resumir_conversacion(conv)
            print(f"- [{resumen['fecha']}] {resumen['titulo']} ({resumen['cantidad_mensajes']} mensajes)")
            total_conversaciones += 1

    print(f"\nTOTAL: {total_conversaciones} conversaciones procesadas en {len(archivos)} archivos")


if __name__ == "__main__":
    procesar_todo()
