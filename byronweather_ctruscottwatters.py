import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import scipy.stats as ss
import math

#def Poisson(mean, e, vals):
#	x = []
#	y = []
#	for v in vals:
#		x.append(v)
#		v = int(v)
#		y.append(((mean ** v) * (e ** -mean))/math.factorial(v))
#	print(x, y)
#	return x, y
def linsearch(rain_xs, rain_probs):
	c = 0
	m = max(rain_probs)
	for x in range(len(rain_probs)):
		if rain_probs[c]  == m:
			break
		c += 1
	print("The highest chance of the predicted most daily rain is {} at {} percent".format(rain_xs[c], rain_xs[c] * rain_probs[c] * 10))
			
def Gaussian(mean, stddev, vals):
	
	x = []
	y = []
	for v in vals:
		normed = 1 / stddev * np.sqrt(2 * np.pi) * np.e ** -(((((v - mean) ** 2)/(2 * stddev) **2)))
		x.append(v)
		y.append(normed)
	return x, y

def Charles():
	plt.figure(0, dpi=145, figsize=[25, 15])
	df = pd.read_csv('byr.csv')
	ax1 = plt.subplot(1, 4, 1)
	plt.plot(df['Year'], df['Max Daily Rain'])
	rain = df['Max Daily Rain']
	mean = np.mean(rain)
	stddev = np.std(rain)
	print(np.mean(rain), np.std(rain))
	plt.title("Charles Truscott Watters. Byron Bay Rainfall")
	ax1.title.set_text("Max Volume of Daily Rainfall Byron Bay. Charles Truscott")
	ax1.set_xlabel("Year")
	ax1.set_ylabel("mm rain")
	ax2 = plt.subplot(1, 4, 2)
	x2, y2 = Gaussian(mean, stddev, rain)
	linsearch(x2, y2)
	print("x {} y {}".format(x2, y2))
	ax2.title.set_text("Normal Distribution as probability of highest volume rain")
	ax2.set_xlabel("Rainfall")
	ax2.set_ylabel('Probability of rainfall')
	plt.scatter(x2, y2)
	ax3 = plt.subplot(1, 4, 3)
	x3, y3 = Gaussian(mean, stddev, sorted(rain))
	ax3.title.set_text("Normal Distribution as probability of highest volume rain")
	ax3.set_xlabel("Rainfall")
	ax3.set_ylabel('Probability of rainfall')
	plt.plot(x3, y3)
	ax4 = plt.subplot(1, 4, 4)
	plt.hist(df['Max Daily Rain'], edgecolor='crimson')
	ax4.title.set_text("Highest Volume of Daily Rainfall Byron Bay")
	ax4.set_xlabel("Volume")
	ax4.set_ylabel("Frequency")
	plt.show()
#	plt.savefig('all.png')
Charles()