import numpy as np
import matplotlib.pyplot as plt
import constants as c
from scipy.optimize import fsolve as solver


n = c.n  # Number of grid points in z direction
dz = c.dz  # Distance between two grid points in centimeter
R1 = c.R1  # Radius of preform in cm
n0 = c.n0  # Refractive index of glass
gamma = c.gamma  # value of absorption coefficient in cm-1
sigma = c.sigma  # stefan boltzman constant in W/m2·K
rho = c.rho  # density of glass in g/cm3
i = np.linspace(0, n, n+1)  # cell index array
z = i*dz  # discretized z axis
L = n*dz  # total length of domain
a = 5  # slider for origin of the curve. change to move the curve on z axis while holding its shape
b = 10  # slider for increasing/decreasing the length of the neck-down region
R = R1*(1/(1 + np.exp(-a + i/(n/b))))

# plt.scatter(i*0.1, R)
# plt.title("Initial neck-down profile")
# plt.xlabel("Distance along the length of preform (cm)")
# plt.ylabel("Radius of the preform (cm)")
# plt.show()


# below function return n-1 equations for the T points which need to be solved
def system_of_T_equations(T):


# below function solves for n-1 T points, adds end points, and returns T array
def T_solver():
