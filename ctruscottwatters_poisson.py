import numpy as np
import matplotlib.pyplot as plt
import math

def Poisson(x, avg):
	return (((np.e) ** (- avg)) * (avg ** x))/(math.factorial(x))
def Charles():
#	for x, y in zip(range(0, 10), [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]):
#		print(Poisson(x, y))
	for x in range(0, 10):
		for e in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]:
			print(Poisson(x, e))
	x1 = [x for x in range(0, 10)]
	y1 = [Poisson(x, 0.5) for x in range(0, 10)]
#	print(x1, y2)
	x2 = [x for x in range(0, 10)]
	y2 = [Poisson(x, 1) for x in range(0, 10)]
	x3 =  [x for x in range(0, 10)]
	y3 = [Poisson(x, 1.5) for x in range(0, 10)]
	x4 =  [x for x in range(0, 10)]
	y4 = [Poisson(x, 2) for x in range(0, 10)]
	x5 =  [x for x in range(0, 10)]
	y5 = [Poisson(x, 2.5) for x in range(0, 10)]
	x6 = [x for x in range(0, 10)]
	y6 = [Poisson(x, 3) for x in range(0, 10)]
	print(x1, y2)
	x7 = [x for x in range(0, 10)]
	y7 = [Poisson(x, 3.5) for x in range(0, 10)]
	x8 =  [x for x in range(0, 10)]
	y8 = [Poisson(x, 4.0) for x in range(0, 10)]
	x9 =  [x for x in range(0, 10)]
	y9 = [Poisson(x, 4.5) for x in range(0, 10)]
	x10 =  [x for x in range(0, 10)]
	y10 = [Poisson(x, 5.0) for x in range(0, 10)]
	plt.figure(0, dpi=150, figsize=[7, 5])
	plt.title("Charles Truscott Watters. Poisson Distribution")
	plt.plot(x1, y1, label='lambda 0.5')
	plt.plot(x2, y2, label='lambda 1')
	plt.plot(x3, y3, label='lambda 1.5')
	plt.plot(x4, y4, label='lambda 2')
	plt.plot(x5, y5, label='lambda 2.5')
	plt.plot(x6, y6, label='lambda 3.0')
	plt.plot(x7, y7, label='lambda 3.5')
	plt.plot(x8, y8, label='lambda 4.0')
	plt.plot(x9, y9, label='lambda 4.5')
	plt.plot(x10, y10, label='lambda 5.0')
	plt.legend()
	plt.savefig('poisson.png')
Charles()