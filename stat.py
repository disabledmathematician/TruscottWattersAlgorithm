import math
import numpy as np
import matplotlib.pyplot as plt

def Poisson(mean, e, vals):
	x = []
	y = []
	for n in range(0, len(vals)):
		x.append(n)
		y.append(((mean ** vals[n]) * (e ** -mean))/math.factorial(vals[n]))
	print(x, y)
	return x, y
	
def Gaussian(mean, stddev, vals):
	
	x = []
	y = []
	for v in vals:
		normed = 1 / stddev * np.sqrt(2 * np.pi) * np.e ** -(((((v - mean) ** 2)/(2 * stddev) **2)))
		x.append(v)
		y.append(normed)
	return x, y
def Charles():
		plt.figure(0, dpi=150, figsize=[15, 10])
		ax1 = plt.subplot(1, 2, 1)
		ax1.title.set_text("Poisson Distribution. Charles Truscott")
		ax1.set_xlabel("x")
		ax1.set_ylabel("P(x)")
		for l in range(1, 12 + 1):
			vals = [n for n in range(0, 12 + 1)]
			x, y = Poisson(l/2, np.e, vals)
			plt.plot(x, y, label="Poisson Distribution with mean of {}".format(l/2))
#		plt.savefig('poisson.png')
#		plt.figure(1,  dpi=150, figsize=[15, 10])
#	for m, d in zip([c for c in range(1, 12)], [t for t in range(1, 12)]):
#	for m in [0.5, 0.75, 1, 1.25, 1.50, 1.75, 2.0]:
#		for v in [0.5, 0.75, 1, 1.25, 1.50, 1.75, 2.0]:
		

		ax2 = plt.subplot(1, 2, 2)
		ax2.title.set_text("Normal Distribution. Charles Truscott")
		ax2.set_xlabel("x")
		ax2.set_ylabel("P(x)")
		for m in [0, 1]:
			for v in [1, 2]:
				x, y = Gaussian(m, v,  [x / 3 for x in range(-30, 30)])
				plt.plot(x, y, label="Normal Distribution with mean {} and standard deviation {}".format(m, v))
#		plt.legend()
#		plt.show()
		plt.savefig('both.png')
#		plt.savefig('normal.png')
Charles()
		