"""
Knowledge Cognition Engine (KCE)
Cliente de Ollama (IA local, gratuita).

Permite que cualquier plugin del KCE le pregunte a un modelo de IA
que corre localmente en la computadora del usuario, sin costo y
sin enviar datos a internet.
"""

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2"


def preguntar_a_ollama(prompt: str) -> str:
    """Envia un prompt al modelo local de Ollama y devuelve la respuesta como texto."""
    respuesta = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False,
        },
        timeout=120,
    )
    respuesta.raise_for_status()
    return respuesta.json()["response"].strip()