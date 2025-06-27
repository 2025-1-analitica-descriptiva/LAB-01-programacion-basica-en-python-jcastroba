"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    counts = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            claves = {item.split(":")[0] for item in line.split("\t")[4].split(",")}
            for k in claves:
                counts[k] = counts.get(k, 0) + 1
    return counts

