# this function takes as input: Radius of fiber.
# it returns: the emissivity at that radius
import numpy as np
def epsilon(R):
    D = 2*R
    if (type(D) == np.float64):
        D = 2 * R
        if D <= 100 * (10 ** (-4)):
            return 0.1
        elif 100 * (10 ** (-4)) < D < 0.2:
            return 62.5078 * ((D) ** 3) + 0.0999
        return 0.6
    e = []
    for d in D:
        if d <= 100 * (10**(-4)):
            e.append(0.1)
        elif 100 * (10**(-4)) < d < 0.2:
            e.append(62.5078*((d)**3) + 0.0999)
        else:
            e.append(0.6)
    return e
