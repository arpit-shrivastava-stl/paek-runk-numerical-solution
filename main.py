import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import constants as c
from scipy.optimize import fsolve as solver
from energy_equation import energy_equation
from glass_viscosity import viscosity

n = c.n  # Number of grid points in z direction
dz = c.dz  # Distance between two grid points in centimeter
R1 = c.R1  # Radius of preform in cm
n0 = c.n0  # Refractive index of glass
gamma = c.gamma  # value of absorption coefficient in cm-1
sigma = c.sigma  # stefan boltzman constant in W/m2·K
rho = c.rho  # density of glass in g/cm3
i = np.linspace(0, n, n + 1)  # cell index array
z = i * dz  # discretized z axis
p = 5  # slider for origin of the curve. change to move the curve on z axis while holding its shape
q = 10  # slider for increasing/decreasing the length of the neck-down region
R = R1 * (1 / (1 + np.exp(-p + i / (n / q))))


# plt.scatter(i*0.1, R)
# plt.title("Initial neck-down profile")
# plt.xlabel("Distance along the length of preform (cm)")
# plt.ylabel("Radius of the preform (cm)")
# plt.show()


# below function return n-1 equations for the T points which need to be solved
def system_of_T_equations(T):
    global R
    global n
    return [energy_equation(T, R, i) for i in range(n - 1)]


# below function solves for n-1 T points, adds end points, and returns T array

output = solver(system_of_T_equations, 1500*np.ones((n - 1,)), full_output=True)

plt.scatter(range(output[0].size), output[0])
plt.show()
