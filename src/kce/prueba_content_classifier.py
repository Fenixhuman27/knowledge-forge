from src.parser.chatgpt_parser import cargar_conversaciones
from src.kce.normalizers import normalizar_chatgpt
from src.kce.pipeline import KCEPipeline
from src.kce.plugins.content_classifier import ContentClassifier

if __name__ == "__main__":
    conversaciones = cargar_conversaciones("conversations-000.json")

    pipeline = KCEPipeline()
    pipeline.registrar_plugin(ContentClassifier())

    for conv in conversaciones[:10]:
        normalizada = normalizar_chatgpt(conv)
        resultados = pipeline.procesar(normalizada)

        for r in resultados:
            print(f"{normalizada.titulo[:50]:50} -> {r.hallazgos}")
