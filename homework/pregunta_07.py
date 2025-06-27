"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



def pregunta_07():
    groups = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            l, v = line.split("\t")[0], int(line.split("\t")[1])
            groups.setdefault(v, []).append(l)
    return [(v, groups[v]) for v in sorted(groups)]

