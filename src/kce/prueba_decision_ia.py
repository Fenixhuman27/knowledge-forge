from src.parser.chatgpt_parser import cargar_conversaciones
from src.kce.normalizers import normalizar_chatgpt
from src.kce.pipeline import KCEPipeline
from src.kce.plugins.decision_detector_ia import DecisionDetectorIA

if __name__ == "__main__":
    conversaciones = cargar_conversaciones("conversations-000.json")

    pipeline = KCEPipeline()
    pipeline.registrar_plugin(DecisionDetectorIA())

    for conv in conversaciones[:5]:
        normalizada = normalizar_chatgpt(conv)
        resultados = pipeline.procesar(normalizada)

        for r in resultados:
            if r.hallazgos:
                print(f"\n=== {normalizada.titulo} ({normalizada.fecha}) ===")
                for h in r.hallazgos:
                    print(f"  - {h[:100]}")

    print("\nListo.")