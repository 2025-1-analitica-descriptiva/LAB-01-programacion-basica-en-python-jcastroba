"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    sums = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            p = line.split("\t")
            total = sum(int(x.split(":")[1]) for x in p[4].split(","))
            sums[p[0]] = sums.get(p[0], 0) + total
    return sums


