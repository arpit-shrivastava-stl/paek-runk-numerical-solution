# Copy constants from paper
# Will be using SI unit system everywhere
# surface_tension = 300  # dyne/cm
surface_tension = 0.3   # N/m
# R1 = 0.6  # cm
R1 = 0.6*(0.01) # m
# R2 = 50*1e-4  # cm
R2 = 50*1e-4*(0.01) # cm
# V2 = 500 # cm/s
V2 = 100*0.01 #m/s
V1 = (R2**2 * V2)/(R1**2)  # m/s
# a = 1.9  # cm
a = 1.9*0.01
# b = 25.4  # cm
b = 25.4*0.01
# l = 4  # cm
l = 4*0.01
# gamma = 2.0  # cm-1 - absorption coefficient
gamma = 2*100 # m-1
# Kr = 0.25  # W/cmC
Kr = 0.25*100 # W/m-K
# Kc = 0.05  # W/cmC
Kc = 0.05*100 # W/m-K
K = Kr + Kc  # W/m-K
# rho = 2.2  # g/cm3
rho = 2.2 * 1000 #kg/m3
# Cp = 0.25  # cal/gC
Cp = 1047 # J/kgC
# Ts = 1600  # C
Ts = 1600 + 273
# Tm = 2000  # C
Tm = 2000 + 273
# T0 = 1100  # C
T0 = 1100 + 273
g = 9.8  # m/s2
alpha = surface_tension
# Emissivity-currently assuming to be constant, but will be later replaced with p function
# epsilon = 0.3 # unitless
# heat transfer coefficient, currently assuming to be p constant, but will be later replaced with p function
# h = 2*1e-2 #W/cm2C
h = 2*1e-2*1e4
sigma = 5.67*1e-8  # in W/m2K4
n0 = 1.47
# Q21 = 1000 # some arbitrary number
p = (16*(n0**2)*sigma)/(3*gamma)

L = 20*0.01 # length of domain in m
dz = 0.01*0.01  # Distance between two grid points in centimeter
n = int(L/dz)  # number of grid points

J0 = 50*1e4
C = 3