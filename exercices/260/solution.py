def euclidean(a, b):
    c = (((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) ** 0.5
    print(c)


def opt_euclidean(d, e):
    import math as m
    f = m.sqrt(m.pow((d[0]-e[0]), 2)+m.pow((d[1]-e[1]), 2))
    print(f)


def np_euclidean(g, h):
    import numpy as np
    i = np.sqrt(((g[0] - h[0]) ** 2) + ((g[1] - h[1]) ** 2))
    print(i)
