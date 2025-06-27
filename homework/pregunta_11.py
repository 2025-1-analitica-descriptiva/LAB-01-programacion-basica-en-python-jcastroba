"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_11():
    sums = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            v = int(line.split("\t")[1])
            for l in line.split("\t")[3].split(","):
                sums[l] = sums.get(l, 0) + v
    return dict(sorted(sums.items()))


