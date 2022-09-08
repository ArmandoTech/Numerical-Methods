import scipy.optimize as opt
import sympy as sp
from sympy import *


def y(x):
    P=40
    T=383
    a=17.16856123
    b=0.022101698
    R=0.08205746

    return  (P+ (a/T**(1/2)*x*(x+b)))*(x-b)-(R*T) 



if __name__ == '__main__':

    respuesta=opt.newton(y, 0.5)
    print(respuesta)