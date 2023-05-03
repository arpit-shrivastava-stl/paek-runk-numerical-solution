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
    Q = Q21()*A
    T0 = c.T0*A
    sigma = c.sigma*A
    Kc = c.Kc*A
    return ((2/R) * (Q - epsilon(R) * sigma * (T ** 4 - T0 ** 4) - c.h * (T - c.T0)))\
        /\
        (Kc + c.p * (T ** 3))
