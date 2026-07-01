import os
import json
from src.parser.chatgpt_parser import cargar_conversaciones, resumir_conversacion

CARPETA_DATOS = "data"
CARPETA_SALIDA = "output"


def buscar_archivos_conversaciones():
    """Busca archivos JSON que contienen conversaciones (empiezan con 'conversations')."""
    archivos = [
        f for f in os.listdir(CARPETA_DATOS)
        if f.startswith("conversations") and f.endswith(".json")
    ]
    return sorted(archivos)


def procesar_todo():
    archivos = buscar_archivos_conversaciones()
    resultados = []

    for archivo in archivos:
        conversaciones = cargar_conversaciones(archivo)
        print(f"\n=== {archivo} ({len(conversaciones)} conversaciones) ===")

        for conv in conversaciones:
            resumen = resumir_conversacion(conv)
            print(f"- [{resumen['fecha']}] {resumen['titulo']} ({resumen['cantidad_mensajes']} mensajes)")
            resultados.append(resumen)

    print(f"\nTOTAL: {len(resultados)} conversaciones procesadas en {len(archivos)} archivos")

    os.makedirs(CARPETA_SALIDA, exist_ok=True)
    ruta_salida = os.path.join(CARPETA_SALIDA, "resumen.json")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    print(f"Resumen guardado en {ruta_salida}")


if __name__ == "__main__":
    procesar_todo()
