"""
Etapa de Deteccion de Relaciones del Knowledge Cognition Engine (KCE).

Recibe una lista de conversaciones (cada una con sus entidades ya detectadas)
y devuelve las relaciones encontradas entre ellas: pares de conversaciones
que comparten al menos una entidad en comun.

Esta es la base que luego alimenta al Knowledge Graph.
"""

from itertools import combinations


def detectar_relaciones(conversaciones_con_entidades):
    """
    conversaciones_con_entidades: lista de tuplas (id_conversacion, set_entidades)

    Devuelve una lista de relaciones, cada una con:
    - id_a, id_b: las dos conversaciones relacionadas
    - entidades_compartidas: lista de entidades en comun
    """
    relaciones = []

    for (id_a, entidades_a), (id_b, entidades_b) in combinations(conversaciones_con_entidades, 2):
        compartidas = set(entidades_a) & set(entidades_b)
        if compartidas:
            relaciones.append({
                "id_a": id_a,
                "id_b": id_b,
                "entidades_compartidas": sorted(compartidas),
            })

    return relaciones
