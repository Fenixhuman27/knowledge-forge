"""
Ejecutor del Knowledge Cognition Engine (KCE).

Recorre todas las conversaciones de todos los archivos de origen,
las normaliza, las pasa por el pipeline con todos los plugins
registrados, y guarda los resultados en output/kce_resultados.json
"""

import os
import json
from src.parser.chatgpt_parser import cargar_conversaciones
from src.kce.normalizers import normalizar_chatgpt
from src.kce.pipeline import KCEPipeline
from src.kce.plugins.decision_detector_hibrido import DecisionDetectorHibrido
from src.kce.plugins.task_detector import TaskDetector
from src.kce.plugins.contradiction_detector import ContradictionDetector

CARPETA_DATOS = "data"
CARPETA_SALIDA = "output"


def buscar_archivos_conversaciones():
    archivos = [
        f for f in os.listdir(CARPETA_DATOS)
        if f.startswith("conversations") and f.endswith(".json")
    ]
    return sorted(archivos)


def construir_pipeline():
    pipeline = KCEPipeline()
    pipeline.registrar_plugin(DecisionDetectorHibrido())
    pipeline.registrar_plugin(TaskDetector())
    pipeline.registrar_plugin(ContradictionDetector())
    return pipeline


def ejecutar():
    archivos = buscar_archivos_conversaciones()
    pipeline = construir_pipeline()

    resultados_totales = []
    conversaciones_procesadas = 0
    conversaciones_con_hallazgos = 0

    for archivo in archivos:
        conversaciones = cargar_conversaciones(archivo)

        for conv in conversaciones:
            normalizada = normalizar_chatgpt(conv)
            resultados = pipeline.procesar(normalizada)
            conversaciones_procesadas += 1

            tiene_hallazgos = any(r.hallazgos for r in resultados)
            if tiene_hallazgos:
                conversaciones_con_hallazgos += 1

            for r in resultados:
                if r.hallazgos:
                    resultados_totales.append({
                        "conversacion_id": r.conversacion_id,
                        "titulo": normalizada.titulo,
                        "fecha": normalizada.fecha,
                        "plugin": r.plugin,
                        "hallazgos": r.hallazgos,
                    })

            if conversaciones_procesadas % 25 == 0:
                print(f"Progreso: {conversaciones_procesadas}/595 conversaciones procesadas...")

    os.makedirs(CARPETA_SALIDA, exist_ok=True)
    ruta_salida = os.path.join(CARPETA_SALIDA, "kce_resultados.json")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(resultados_totales, f, ensure_ascii=False, indent=2)

    print(f"Conversaciones procesadas: {conversaciones_procesadas}")
    print(f"Conversaciones con hallazgos: {conversaciones_con_hallazgos}")
    print(f"Resultados guardados en: {ruta_salida}")


if __name__ == "__main__":
    ejecutar()
