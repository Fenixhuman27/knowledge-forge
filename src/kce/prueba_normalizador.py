"""
Script temporal para verificar que el normalizador de ChatGPT
funciona correctamente antes de seguir construyendo el motor.
"""

from src.parser.chatgpt_parser import cargar_conversaciones
from src.kce.normalizers import normalizar_chatgpt

if __name__ == "__main__":
    conversaciones = cargar_conversaciones("conversations-000.json")
    primera = conversaciones[0]

    normalizada = normalizar_chatgpt(primera)

    print(f"ID: {normalizada.id}")
    print(f"Titulo: {normalizada.titulo}")
    print(f"Fecha: {normalizada.fecha}")
    print(f"Origen: {normalizada.origen}")
    print(f"Cantidad de mensajes: {len(normalizada.mensajes)}")
    print()
    print("Primer mensaje:")
    print(f"  Autor: {normalizada.mensajes[0].autor}")
    print(f"  Texto: {normalizada.mensajes[0].texto[:100]}...")
