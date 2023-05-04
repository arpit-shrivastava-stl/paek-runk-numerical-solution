import constants as c
from Q21 import Q21
from emissivity import epsilon
from R_and_R_dash import R as r
import numpy as np
def g(x, y):
    T = y
    R = r(x)
    n = len(R)

    A = np.ones(n)
    Q = Q21(R)
    T0 = c.T0*A
    sigma = c.sigma*A
    eps = epsilon(R)
    Kc = c.Kc*A
    return ((2/R) * (Q - eps * (sigma * (T ** 4 - T0 ** 4)) - c.h * (T - T0)))\
        /\
        (Kc + c.p * (T ** 3))
