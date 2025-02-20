import numpy as np
import matplotlib.pyplot as plt
import math

def Poisson(x, avg):
	return (((np.e) ** (- avg)) * (avg ** x))/(math.factorial(x))
def Charles():
	for x, y in zip(range(0, 10), [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]):
		print(Poisson(x, y))
	
Charles()