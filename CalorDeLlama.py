import math
import sympy
from IPython.display import display

T = sympy.symbols('T')

dA = 1.131
dB = 0.019225
dC = -5.561e-6
dD = 0
dHr = 75438 # J/mol
R = 8.314 #J/mol

integral = sympy.integrate(dA+dB*T+dC*T**2+dD*T**-2, (T,298.15,T))
display(integral)

ecuacion = sympy.Eq(dHr, -R*integral)
display(ecuacion)

# Resolver para T
Tflama= sympy.solve(ecuacion,T)
print(Tflama)

print("La temperatura de flama adiabática es:")
print((Tflama[2]))