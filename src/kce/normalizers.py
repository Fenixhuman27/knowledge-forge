"""
Knowledge Cognition Engine (KCE)
Normalizadores.

Cada funcion aqui toma una conversacion en su formato original
(ChatGPT, Claude, Gemini, etc.) y la convierte al formato estandar
definido en schema.py.
"""

from src.kce.schema import NormalizedConversation, NormalizedMessage
from src.parser.chatgpt_parser import extraer_mensajes, resumir_conversacion


def normalizar_chatgpt(conversacion: dict) -> NormalizedConversation:
    """Convierte una conversacion cruda de ChatGPT al formato universal del KCE."""
    resumen = resumir_conversacion(conversacion)
    mensajes_originales = extraer_mensajes(conversacion)

    mensajes = [
        NormalizedMessage(
            autor=m["autor"],
            texto=m["texto"],
            timestamp=m["create_time"],
        )
        for m in mensajes_originales
    ]

    return NormalizedConversation(
        id=conversacion.get("conversation_id", ""),
        titulo=resumen["titulo"],
        fecha=resumen["fecha"],
        origen="chatgpt",
        mensajes=mensajes,
        metadata={},
    )
