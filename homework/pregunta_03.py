"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    sums = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            parts = line.split("\t")
            l, v = parts[0], int(parts[1])
            sums[l] = sums.get(l, 0) + v
    return sorted(sums.items())


