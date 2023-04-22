from constants import Ts, dz, n
from f import f
from g import g


def energy_equation(T, R, i):
    # here T is the temperature array
    if i == 0:
        return (Ts + T[i + 1] - 2 * T[i]) / (dz ** 2) + \
            f(T[i], R, i+1) * ((T[i + 1] + Ts) / (2 * dz)) + \
            g(T[i], R, i+1)
    # when calling f and g, i+1 index is used instead of i
    # this is because for R array, the i index corresponds to
    # one place ahead, because it has extra element at end point.
    # so for T[0], R[1] should be used. here T is not the final
    # solution, but the array of only the temperatures which are
    # needed to be solved.
    elif i == n - 2:
        return (T[i - 1] + Ts - 2 * T[i]) / (dz ** 2) + \
            f(T[i], R, i+1) * ((Ts + T[i - 1]) / (2 * dz)) + \
            g(T[i], R, i+1)
    return (T[i - 1] + T[i + 1] - 2 * T[i]) / (dz ** 2) + \
        f(T[i], R, i+1) * ((T[i + 1] + T[i - 1]) / (2 * dz)) + \
        g(T[i], R, i+1)
