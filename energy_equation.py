from constants import Ts, dz, n
from f import f
from g import g


def energy_equation(T, R, i):
    # here T is the temperature array
    if i == 0:
        return (Ts + T[i + 1] - 2 * T[i]) / (dz ** 2) + \
            f(T[i], R, i) * ((T[i + 1] + Ts) / (2 * dz)) + \
            g(T[i], R, i)

    elif i == n - 2:
        return (T[i - 1] + Ts - 2 * T[i]) / (dz ** 2) + \
            f(T[i], R, i) * ((Ts + T[i - 1]) / (2 * dz)) + \
            g(T[i], R, i)
    return (T[i - 1] + T[i + 1] - 2 * T[i]) / (dz ** 2) + \
        f(T[i], R, i) * ((T[i + 1] + T[i - 1]) / (2 * dz)) + \
        g(T[i], R, i)
