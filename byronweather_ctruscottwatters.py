import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import scipy.stats as ss
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
#	print(df['Year'], df['Max Daily Rain'])
#	x = df['Year'].to_numpy().reshape(-1, 1)
#	x = df['Year'].to_numpy()
#	X_plot = df['Year'].to_numpy().reshape(-1, 1)
#	y = df["Max Daily Rain"].to_numpy().reshape(-1, 1)
#	frame = [x, y]
#	x = pd.concat(frame, axis=1)
#	plt.scatter(df['Year'], y)
#	plt.show()
#	x2 = []
#	y2 = []
#	poly = PolynomialFeatures(degree=3, include_bias=False)
#	poly_features = poly.fit_transform(x)
#	poly.fit(x)
#	poly_reg_model = LinearRegression()
#	poly_reg_model.fit(poly_features, y)
#	y_predicted = poly_reg_model.predict(poly_features)
#	plt.plot(x, y_predicted)
#	    for n in range(2024, 2030):
#	    	 y_plot = model.predict(n)
#	    	 x2.append(n)
#	    	 y2.append(y_plot)
#	    plt.plot(x2, y2)
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
#	plt.hist(df['Max Daily Rain'])
#	x1, y1 = Poisson(mean, np.e, rain)
	ax2 = plt.subplot(1, 4, 2)
	x2, y2 = Gaussian(mean, stddev, rain)
	ax2.title.set_text("Normal Distribution as probability of highest volume rain")
	ax2.set_xlabel("Rainfall")
	ax2.set_ylabel('Probability of rainfall')
	plt.scatter(x2, y2)
	ax3 = plt.subplot(1, 4, 3)
	x3, y3 = Gaussian(mean, stddev, [rf for rf in range(0, 300)])
	ax3.title.set_text("Normal Distribution as probability of highest volume rain")
	ax3.set_xlabel("Rainfall")
	ax3.set_ylabel('Probability of rainfall')
	plt.plot(x3, y3)
#	plt.plot(x1, y1)
#	plt.hist(y2)
	ax4 = plt.subplot(1, 4, 4)
	plt.hist(df['Max Daily Rain'], edgecolor='crimson')
	ax4.title.set_text("Highest Volume of Daily Rainfall Byron Bay")
	ax4.set_xlabel("Volume")
	ax4.set_ylabel("Frequency")

#	plt.plot(x, y_predicted)

#	plt.show()
#	plt.title("Charles Truscott Watters")
	plt.savefig('all.png')
Charles()