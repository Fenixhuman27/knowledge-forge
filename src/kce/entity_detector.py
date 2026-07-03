"""
Etapa de Deteccion de Entidades del Knowledge Cognition Engine (KCE).

Recibe una ConversacionNormalizada y devuelve una lista de entidades
detectadas (nombres propios y terminos relevantes).

Esta version usa reglas simples (mayusculas, frecuencia de palabras).
En el futuro, esta misma funcion podra ser reemplazada por una version
que use un modelo de IA, sin que el resto del sistema deba cambiar.
"""

import re
from collections import Counter

PALABRAS_IGNORADAS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "del", "en", "y", "a", "que", "es", "por", "para",
    "con", "no", "se", "su", "sus", "lo", "como", "mas", "pero",
}


def detectar_entidades(conversacion_normalizada):
    """Detecta nombres propios y terminos relevantes en una conversacion."""
    texto_completo = " ".join(m.texto for m in conversacion_normalizada.mensajes)

    palabras = re.findall(r"\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]{2,}\b", texto_completo)

    contador = Counter(
        p for p in palabras
        if p.lower() not in PALABRAS_IGNORADAS
    )

    entidades = [palabra for palabra, frecuencia in contador.most_common(10)]
    return entidades
