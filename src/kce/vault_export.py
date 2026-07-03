"""
Knowledge Cognition Engine (KCE)
Exportador de resultados a Obsidian.

Convierte los resultados guardados en output/kce_resultados.json
en notas de Obsidian, organizadas por plugin, y enlazadas a la
nota original de la conversacion.
"""

import json
import os
import re

CARPETA_RESULTADOS = "output/kce_resultados.json"
CARPETA_VAULT_HALLAZGOS = "vault/hallazgos"


def limpiar_nombre_archivo(texto):
    texto = texto.strip()
    texto = re.sub(r'[\\/*?:"<>|]', "", texto)
    texto = texto[:80]
    return texto if texto else "Sin titulo"


def nombre_nota_original(titulo, fecha, conversacion_id):
    """Debe coincidir exactamente con el formato usado en obsidian_export.py"""
    nombre_seguro = limpiar_nombre_archivo(titulo)
    id_corto = conversacion_id[:8]
    return f"{fecha} - {nombre_seguro} - {id_corto}"


def generar_notas_hallazgos():
    with open(CARPETA_RESULTADOS, "r", encoding="utf-8") as f:
        resultados = json.load(f)

    os.makedirs(CARPETA_VAULT_HALLAZGOS, exist_ok=True)
    contador = 0

    for r in resultados:
        nombre_original = nombre_nota_original(r["titulo"], r["fecha"], r["conversacion_id"])
        nombre_archivo = limpiar_nombre_archivo(f"{r['plugin']} - {r['fecha']} - {r['titulo']}")
        ruta_nota = os.path.join(CARPETA_VAULT_HALLAZGOS, f"{nombre_archivo}.md")

        etiqueta_plugin = r["plugin"]

        lineas = []
        lineas.append("---")
        lineas.append(f"plugin: {etiqueta_plugin}")
        lineas.append(f"fecha: {r['fecha']}")
        lineas.append("tags:")
        lineas.append(f"  - {etiqueta_plugin}")
        lineas.append("---")
        lineas.append("")
        lineas.append(f"# {etiqueta_plugin.replace('_', ' ').title()}")
        lineas.append("")
        lineas.append(f"Conversacion origen: [[{nombre_original}]]")
        lineas.append("")
        lineas.append("## Hallazgos")
        lineas.append("")
        for h in r["hallazgos"]:
            lineas.append(f"- {h}")
        lineas.append("")

        with open(ruta_nota, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas))
        contador += 1

    return contador


if __name__ == "__main__":
    total = generar_notas_hallazgos()
    print(f"Se crearon {total} notas de hallazgos en {CARPETA_VAULT_HALLAZGOS}")
