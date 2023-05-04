import numpy as np
from f import f
from g import g
import constants as c
import matplotlib
matplotlib.use('TkAgg')
from glass_viscosity import viscosity
def fun(x, y):
    return np.vstack((y[1], -f(x, y[0])*y[1] - g(x, y[0])))

def bc(ya, yb):
    return np.array([ya[0]-c.Ts, yb[0]-c.Ts])

x = np.linspace(0, c.L, 20)
y_a = np.ones((2, x.size))
y_b = np.ones((2, x.size))
y_a[0] = c.Ts
y_b[0] = c.T0

from scipy.integrate import solve_bvp
res_a = solve_bvp(fun, bc, x, y_a)
res_b = solve_bvp(fun, bc, x, y_b)

x_plot = np.linspace(0, c.L, 100)
y_plot_a = res_a.sol(x_plot)[0]
y_plot_b = res_b.sol(x_plot)[0]
import matplotlib.pyplot as plt
plt.plot(x_plot, y_plot_a, label='y_a')
plt.plot(x_plot, y_plot_b, label='y_b')
# plt.plot(x_plot, viscosity(y_plot_b), label='viscosity')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()