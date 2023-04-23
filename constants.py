# Copy constants from paper
surface_tension = 300  # dyne/cm
R1 = 0.6  # cm
R2 = 50*1e-4  # cm
V2 = 100 # cm/s
V1 = (R2**2 * V2)/(R1**2)  # cm/s
a = 1.9  # cm
b = 25.4  # cm
l = 4  # cm
gamma = 2.0  # cm-1 - absorption coefficient
Kr = 0.25  # W/cmC
Kc = 0.05  # W/cmC
K = Kr + Kc  # W/cmC
rho = 2.2  # g/cm3
Cp = 0.25  # cal/gC
Ts = 1600  # C
Tm = 2000  # C
T0 = 1100  # C
g = 980  # cm/s2
alpha = 300  #dyn/cm
# Emmisivity- currently assuming to be constant, but will be later replaced with a function
epsilon = 0.3 # unitless
# heat transfer coefficient, currently assuming to be a constant, but will be later replaced with a function
h = 2*1e-2 #W/cm2C
sigma = 5.67*1e-4  # in kg cm2 s-2 K-1
n0 = 1.47
Q21 = 10 # some arbitrary number
p = (16*(n0**2)*sigma)/(3*gamma)

L = 20 # length of domain in cm
dz = 0.1  # Distance between two grid points in centimeter
n = int(L/dz)  # number of grid points