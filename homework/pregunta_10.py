"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    res = []
    with open("files/input/data.csv", "r") as f:
        for line in f:
            p = line.split("\t")
            res.append((p[0], len(p[3].split(",")), len(p[4].split(","))))
    return res


