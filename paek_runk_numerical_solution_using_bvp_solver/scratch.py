from R_and_R_dash import R
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,1,100)
y = R(x)
plt.plot(x,y)
plt.show()