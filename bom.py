# -*- coding: utf-8 -*-
"""
BOM Data Notebook
Charles Truscott Watters
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import scipy.stats as ss
#import chardet
def main():
    csv = pd.read_csv('rainfall_allyears.csv')
    years = []
    maxtemps = []
    dates = []
    print(csv)
    print(csv[['Year','Rainfall amount (millimetres)']])
    for y in ['2003','2004','2005','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',  '2017', '2018', '2019','2020', '2021', '2022', '2023', '2024']:
#       print(csv.loc[csv['Year'] == y and csv['Rainfall amount (millimetres)'] == max(csv['Rainfall amount (millimetres)'])])
#       print(csv.loc[csv['Year'] == int(y)])
        temp = csv.loc[csv['Year'] == int(y)]
        temp = temp.fillna(0)
#        ddmmyy = csv.loc[csv['Rainfall amount (millimetres)'] ==  max(temp['Rainfall amount (millimetres)'])]
#       print(max(temp['Rainfall amount (millimetres)']))
        ddmmyy = temp.loc[temp['Rainfall amount (millimetres)'] ==  max(temp['Rainfall amount (millimetres)'])]
#        print('{} {} {}'.format(y, int(ddmmyy['Month']), int(ddmmyy['Day'])))
        dates.append('{}/{}/{}'.format(int(ddmmyy['Day']), int(ddmmyy['Month']), y))
        print('Year {} Highest Rainfall Volume that year {}'.format(y, max(temp['Rainfall amount (millimetres)'])))
        years.append(y)
#        print(ddmmyy)
        maxtemps.append(max(temp['Rainfall amount (millimetres)']))
    df = pd.DataFrame({'Year': years, 'Max Daily Rain': maxtemps, 'Date': dates})
    print(df)
    df.to_csv('ctruscott_byronrainfall.csv')

    print(csv.columns)
    plt.figure(0, dpi=150, figsize=[12, 7])
    plt.plot(years, maxtemps, color='black', label='Highest Recorded Rainfall')
    plt.xlabel('Year')
    plt.ylabel('Highest Recorded Rainfall for that year, in millimetres a day')
    plt.title("Byron Bay Rainfall, BoM Data. Charles Truscott Watters")
    plt.savefig('most_rainfall_21years_byronbay.png')

def count():
	ds = []
	ms = []
	fh = open('ctruscott_byronrainfall.csv', 'r+')
	for line in fh.readlines():
		if len(line.strip('\n').split('/')) > 1:
			ds.append(line.strip('\n').split('/'))
			
	print(ds)
	for e in ds:
		ms.append(e[1])
	plt.figure(0, dpi=140, figsize=[10, 7])
	plt.hist(ms, edgecolor='black', color='blue')
	plt.title("Frequency of month which had the day of the greatest rainfall Byron Bay 2003 to 2024")
	plt.xlabel("Month")
	plt.ylabel("How many times has the month had the year's highest daily rainfall 2003 to 2024")
	plt.savefig('hist_byronrain.png')
count()