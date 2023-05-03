from numpy import exp


def viscosity(T):
    return exp(-5.884 + 27115/(T+273))

