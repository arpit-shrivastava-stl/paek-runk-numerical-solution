# Don't call this equation on end points of domain, i.e. i=0 or i=n

import constants as c
from R_and_R_dash import R as r, R_dash as r_dash

def f(x, y):
    T = y
    R = r(x)
    R_dash = r_dash(x)
    # T is p number here, not the temperature array
    return (3 * c.p * (T ** 2) +
            (c.Kc + c.p * (T ** 3)) * (2 / R) * R_dash
            - (c.rho * c.Cp * (c.R1 ** 2) * c.V1) / (R ** 2))\
        /\
        (c.Kc + c.p * (T ** 3))

