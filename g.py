import constants as c


def g(T, R, i):
    return ((2/R[i]) * (c.Q21 - c.epsilon * c.sigma * (T ** 4 - c.T0 ** 4) - c.h * (T - c.T0)))\
        /\
        (c.Kc + c.p * (T ** 3))
