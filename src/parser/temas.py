TEMAS = {
    "trabajo": ["trabajo", "empleo", "jefe", "oficina", "chofer", "laboral"],
    "salud": ["salud", "medico", "sintoma", "dolor", "enfermedad", "hierro", "vitamina"],
    "relaciones": ["pareja", "matrimonio", "amor", "relacion", "familia"],
    "tecnologia": ["chatbot", "programacion", "codigo", "ia", "inteligencia artificial", "software"],
    "politica": ["politica", "ideologia", "izquierda", "derecha", "gobierno", "conflicto"],
    "religion": ["religion", "teologia", "dios", "biblia", "fe"],
    "musica": ["musica", "cancion", "instrumento", "banda"],
    "humor": ["humor", "chiste", "gracioso", "meme"],
    "uruguay": ["uruguay", "montevideo"],
    "redes_sociales": ["redes sociales", "twitter", "instagram", "facebook", "lgbt"],
}


def detectar_temas(titulo):
    """Devuelve una lista de temas detectados en un titulo, buscando palabras clave."""
    titulo_normalizado = titulo.lower()
    temas_encontrados = []

    for tema, palabras_clave in TEMAS.items():
        for palabra in palabras_clave:
            if palabra in titulo_normalizado:
                temas_encontrados.append(tema)
                break

    return temas_encontrados
