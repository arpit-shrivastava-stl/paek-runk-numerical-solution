import numpy as np
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
a = 5  # slider for origin of the curve. change to move the curve on z axis while holding its shape
b = 10  # slider for increasing/decreasing the length of the neck-down region
R = R1 * (1 / (1 + np.exp(-a + i / (n / b))))


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

output = solver(system_of_T_equations, c.Ts*np.ones((n - 1,)), full_output=True, factor=0.1, epsfcn=0.001)
print(output[2])
print(output[3])
T_filtered = []
value_filtered = []
for i in range(output[0].__len__()):
    if 2000 > output[0][i] > 0:
        T_filtered.append(output[0][i])
        value_filtered.append(output[1]['fvec'][i])
plt.scatter(range(T_filtered.__len__()), T_filtered)
# plt.scatter(range(value_filtered.__len__()), value_filtered)
plt.show()
