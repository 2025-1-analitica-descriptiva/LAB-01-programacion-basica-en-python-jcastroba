"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    counts = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            month = line.split("\t")[2].split("-")[1]
            counts[month] = counts.get(month, 0) + 1
    return sorted(counts.items())


