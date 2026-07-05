from src.parser.chatgpt_parser import cargar_conversaciones
from src.kce.normalizers import normalizar_chatgpt
from src.kce.pipeline import KCEPipeline
from src.kce.plugins.decision_detector_ia import DecisionDetectorIA

if __name__ == "__main__":
    conversaciones = cargar_conversaciones("conversations-000.json")

    pipeline = KCEPipeline()
    pipeline.registrar_plugin(DecisionDetectorIA())

    encontrada = False
    for conv in conversaciones:
        normalizada = normalizar_chatgpt(conv)
        if "Veracidad" in normalizada.titulo:
            encontrada = True
            print(f"Analizando: {normalizada.titulo}")
            resultados = pipeline.procesar(normalizada)
            for r in resultados:
                print(f"Hallazgos: {len(r.hallazgos)}")
                for h in r.hallazgos:
                    print(f"  - {h[:150]}")
            break

    if not encontrada:
        print("No se encontro esa conversacion en este archivo.")
