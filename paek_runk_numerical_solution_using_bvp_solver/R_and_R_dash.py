import constants as c
import numpy as np

def R(x):
    p = 5  # slider for origin of the curve. change to move the curve on z axis while holding its shape
    q = 2.5  # slider for increasing/decreasing the length of the neck-down region
    return c.R1 * (1 / (1 + np.exp(-p + x / (c.L / q))))

def R_dash(x):
    p = 5  # slider for origin of the curve. change to move the curve on z axis while holding its shape
    q = 10  # slider for increasing/decreasing the length of the neck-down region
    return -(q*c.R1*np.exp((q*x)/c.L -p))/(c.L*(np.exp((q*x)/c.L -p) + 1)**2)