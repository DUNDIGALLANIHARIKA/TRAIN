# -*- coding: utf-8 -*-
"""
Created on Tue May 18 05:55:53 2021

@author: Dniharika
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Year=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
##Temp_I=temperature index
Temp_I=[0.72,0.61,0.65,0.68,0.75,0.90,1.02,0.93,0.85,0.99,1.02]

plt.plot(Year,Temp_I)
plt.xlabel('Year')
plt.ylabel('Temp_I')
plt.title('Gloabal Warming',{'fontsize':12,'horizontalalignment':'right'})
plt.show()

Month=['Jan','Feb','Mar','Apr','May','june','July','Aug','Sep','Oct','Nov','Dec']
Cust1=[12,13,9,8,7,8,8,7,6,5,8,10]
Cust2=[14,16,11,7,6,6,7,6,5,8,9,12]

plt.plot(Month,Cust1,color='red',label='Customer1',marker='o')
plt.plot(Month,Cust2,color='blue',label='Customer2',marker='^')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Building Consumption')
plt.legend(loc='upper right')
plt.show()

plt.subplot(1,2,1)
plt.plot(Month,Cust1,color='red',label='Customer1',marker='o')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Building Consumption of Cust1')
plt.show()

plt.subplot(1,2,2)
plt.plot(Month,Cust2,color='blue',label='Customer2',marker='^')
plt.xlabel('Month')
plt.title('Building Consumption of Cust2')
plt.show()

plt.scatter(Month,Cust1,color='red',label='Customer1')
plt.scatter(Month,Cust2,color='blue',label='Customer2')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Scatter Plot of Building Consumption')
plt.grid()
plt.legend()
plt.show()

plt.hist(Cust1,bins=10,color='green')
##plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Histogram')
plt.show()

plt.bar(Month,Cust1,width=0.8,color='b')
plt.show()

plt.bar(Month,Cust1,color='red',label='customer1')
plt.bar(Month,Cust2,color='blue',label='Customer2')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Bar Chart')
plt.legend()
plt.show()

bar_width=0.4
month_b=np.arange(12)

plt.bar(month_b,Cust1,bar_width,color='blue',label='Customer1')
plt.show()

bar_width=0.4
month_b=np.arange(12)
plt.bar(month_b,Cust1,bar_width,color='blue',label='Customer1')
plt.bar(month_b+bar_width,Cust2,bar_width,color='red',label='Customer2')
plt.xlabel('Month')
plt.ylabel('Electricity Consumption')
plt.title('Bar Chart')
plt.legend()
plt.show()

bar_width=0.4
month_b=np.arange(12)
plt.bar(month_b,Cust1,bar_width,color='blue',label='Customer1')
plt.bar(month_b+bar_width,Cust2,bar_width,color='red',label='Customer2')
plt.xticks(month_b,('Jan','Feb','Mar','Apr','May','june','July','Aug','Sep','Oct','Nov','Dec'))
plt.ylabel('Electricity Consumption')
plt.title('Bar Chart')
plt.legend()
plt.show()

bar_width=0.4
month_b=np.arange(12)
plt.bar(month_b,Cust1,bar_width,color='blue',label='Customer1')
plt.bar(month_b+bar_width,Cust2,bar_width,color='red',label='Customer2')
plt.xticks(month_b+(bar_width)/12,('Jan','Feb','Mar','Apr','May','june','July','Aug','Sep','Oct','Nov','Dec'))
plt.ylabel('Electricity Consumption')
plt.title('Bar Chart')
plt.legend()
plt.show()

plt.boxplot(Cust1,notch=True,vert=False)

plt.boxplot(Cust1,notch=False,vert=True)

plt.boxplot([Cust1,Cust2],patch_artist=True,boxprops=dict(facecolor='red',color='black'),
            whiskerprops=dict(color='green'),capprops=dict(color='blue'),
            medianprops=dict(color='yellow'))
plt.show()