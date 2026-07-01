import os

CARPETA_DATOS = "data"

def buscar_archivos_json():
    archivos = [f for f in os.listdir(CARPETA_DATOS) if f.endswith(".json")]
    return sorted(archivos)

if __name__ == "__main__":
    archivos = buscar_archivos_json()
    print(f"Se encontraron {len(archivos)} archivos JSON")
    for archivo in archivos:
        print(archivo)