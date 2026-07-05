from src.kce.ollama_client import preguntar_a_ollama

if __name__ == "__main__":
    try:
        respuesta = preguntar_a_ollama("Decime hola en una palabra")
        print("Respuesta de la IA local:")
        print(respuesta)
    except Exception as e:
        print("ERROR:")
        print(e)
