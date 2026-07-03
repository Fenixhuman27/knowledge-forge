"""
Etapa de Normalizacion del Knowledge Cognition Engine (KCE).

Convierte conversaciones en formato original (ChatGPT, Claude, Gemini, etc.)
a la estructura estandar ConversacionNormalizada, definida en schema.py.

Esta es la unica capa que conoce los formatos originales.
A partir de aqui, ningun otro modulo del KCE necesita saber
de donde vino la conversacion.
"""

from src.kce.schema import ConversacionNormalizada, Mensaje
from src.parser.chatgpt_parser import extraer_mensajes, resumir_conversacion


def normalizar_conversacion_chatgpt(conversacion_original):
    """Convierte una conversacion cruda de ChatGPT en una ConversacionNormalizada."""
    resumen = resumir_conversacion(conversacion_original)
    mensajes_crudos = extraer_mensajes(conversacion_original)

    mensajes = [
        Mensaje(
            autor=m["autor"],
            texto=m["texto"],
            fecha=str(m["create_time"]) if m["create_time"] else None,
        )
        for m in mensajes_crudos
    ]

    return ConversacionNormalizada(
        id=conversacion_original.get("conversation_id", ""),
        titulo=resumen["titulo"],
        fecha=resumen["fecha"],
        origen="chatgpt",
        mensajes=mensajes,
        temas=[],
        metadatos={},
    )
