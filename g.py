import constants as c
from Q21 import Q21
from emissivity import epsilon

def g(T, R, i):
    return ((2/R[i]) * (Q21(R, i) - epsilon(R[i]) * c.sigma * (T ** 4 - c.T0 ** 4) - c.h * (T - c.T0)))\
        /\
        (c.Kc + c.p * (T ** 3))
