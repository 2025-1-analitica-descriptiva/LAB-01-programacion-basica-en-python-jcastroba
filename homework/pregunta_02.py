"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    counts = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            l = line.split("\t")[0]
            counts[l] = counts.get(l, 0) + 1
    return sorted(counts.items())


