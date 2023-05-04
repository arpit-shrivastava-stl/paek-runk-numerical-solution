import constants as c
from emissivity import epsilon
import scipy.integrate as integrate
from math import exp
import numpy as np

def J(x):
    J = c.J0*exp(-c.C*(((x - c.b/2 + c.l)/(c.b))**2))
    return J

def integrand(x, R, R_dash, i):
    return ( J(x)* (-R_dash*(x-i*c.dz) + (c.a - R) ))/\
           (((x-i*c.dz)**2 + (c.a - R)**2)**2)


def Q21(R):
    q = [0]
    for i in range(1, len(R)-1):
        R_dash = (R[i+1] - R[i-1])/(2*c.dz)
        first_term = (2*epsilon(R[i])*(c.a - R[i])*c.a)/\
        ((1+R_dash**2)**(0.5))
        second_term = integrate.quad(integrand, -c.l, c.b-c.l,
                                     args=(R[i], R_dash, i))
        q.append(first_term*second_term[0])
    q[0] = q[1]
    q.append(q[len(q)-1])
    return q