"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    stats = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            l, v = line.split("\t")[0], int(line.split("\t")[1])
            if l not in stats:
                stats[l] = [v, v]
            else:
                stats[l][0] = max(stats[l][0], v)
                stats[l][1] = min(stats[l][1], v)
    return [(l, mx, mn) for l, (mx, mn) in sorted(stats.items())]

