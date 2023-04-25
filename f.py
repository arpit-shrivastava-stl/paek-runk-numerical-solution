# Don't call this equation on end points of domain, i.e. i=0 or i=n

import constants as c


def f(T, R, i):
    # T is p number here, not the temperature array
    return (3 * c.p * (T ** 2) +
            (c.Kc + c.p * (T ** 3)) * (2 / R[i]) * ((R[i + 1] + R[i - 1]) / (2 * c.dz))
            - (c.rho * c.Cp * (c.R1 ** 2) * c.V1) / (R[i] ** 2))\
        /\
        (c.Kc + c.p * (T ** 3))

