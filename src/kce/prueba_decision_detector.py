"""
Script temporal para probar el Decision Detector con conversaciones
reales antes de conectarlo al pipeline completo.
"""

from src.parser.chatgpt_parser import cargar_conversaciones
from src.kce.normalizers import normalizar_chatgpt
from src.kce.pipeline import KCEPipeline
from src.kce.plugins.decision_detector import DecisionDetector

if __name__ == "__main__":
    conversaciones = cargar_conversaciones("conversations-000.json")

    pipeline = KCEPipeline()
    pipeline.registrar_plugin(DecisionDetector())

    conversaciones_con_decisiones = 0

    for conv in conversaciones[:50]:
        normalizada = normalizar_chatgpt(conv)
        resultados = pipeline.procesar(normalizada)

        for r in resultados:
            if r.hallazgos:
                conversaciones_con_decisiones += 1
                print(f"\n=== {normalizada.titulo} ({normalizada.fecha}) ===")
                for h in r.hallazgos:
                    print(f"  - {h[:100]}")

    print(f"\n\nTOTAL: {conversaciones_con_decisiones} conversaciones con decisiones detectadas (de las primeras 50)")
