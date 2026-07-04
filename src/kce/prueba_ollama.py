from src.kce.ollama_client import preguntar_a_ollama

if __name__ == "__main__":
    respuesta = preguntar_a_ollama("Decime hola en una palabra")
    print("Respuesta de la IA local:")
    print(respuesta)
