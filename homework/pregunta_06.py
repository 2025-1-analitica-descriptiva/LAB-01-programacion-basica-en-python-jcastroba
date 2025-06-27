"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    stats = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            for item in line.split("\t")[4].strip().split(","):
                k, val = item.split(":")
                v = int(val)
                if k not in stats:
                    stats[k] = [v, v]
                else:
                    stats[k][0] = min(stats[k][0], v)
                    stats[k][1] = max(stats[k][1], v)
    return [(k, mn, mx) for k, (mn, mx) in sorted(stats.items())]


