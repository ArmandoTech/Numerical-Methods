
from scipy import integrate
import numpy as np

f = lambda x: (0.697-1)/x
integral=integrate.quadrature(f, 0, 40)
print(np.exp(integral))