# -*- coding: utf-8 -*-
"""
Created on Fri May 21 20:00:19 2021

@author: Dniharika
"""

import pandas as pd
data_set1=pd.read_csv("Data_Set.csv")
data_set1.head()

data_set2=pd.read_csv("Data_Set.csv",header=2)##header=2 gives data without first two rows

data_set3=data_set2.rename(columns={'Temperature':'Temp'})

data_set4=data_set3.drop('No. Occupants',axis=1)
##data_set3.drop('No. Occupants',axis=1,inplace=True)##used when we dont want to create a a new variable

data_set5=data_set4.drop(2,axis=0)

data_set6=data_set5.reset_index(drop=True)
##data_set5.reset_index()##creates a new index column along with previous index

data_set6.describe()

min_item=data_set6['E_Heat'].min()

data_set6['E_Heat'][data_set6['E_Heat']==min_item]##to know the row number

data_set6['E_Heat'].replace(-4,21,inplace=True)

##covariance
data_set6.cov()

import seaborn as sn

sn.heatmap(data_set6.corr())

##Nan is diplayed in data which means NOT A NUMBER and NUll is displayed when it is empty

##missing values

data_set6.info()

import numpy as np 

data_set7=data_set6.replace('!',np.NaN)
data_set7.info()

data_set7=data_set7.apply(pd.to_numeric)
data_set7.info()

data_set7.isnull()
data_set7.drop(13,axis=0,inplace=True)
data_set7.dropna(axis=0,inplace=True)

import numpy as np 

data_set7=data_set6.replace('!',np.NaN)
data_set7.info()

data_set8=data_set7.fillna(method='ffill')##forward fill 
##data_set8=data_set7.fillna(method='bfill')##backward fill

from sklearn.impute import SimpleImputer 

M_Var=SimpleImputer(missing_values=np.nan,strategy='mean')
M_Var.fit(data_set7)

data_set9=M_Var.transform(data_set7)

##outlier detection

data_set8.boxplot()

data_set8['E_Plug'].quantile(0.25)  
data_set8['E_Plug'].quantile(0.75)  

""""""

Q1=21.25 
Q3=33.75 
IQR=33.75-21.25=12.5

MILD OUTLIER

Lower Bound=Q1-1.5*IQR = 21.25-1.5(12.5) = 21.25-18.75 = 2.5
Upper Bound=Q3+1.5*IQR = 33.75+1.5(12.5) = 33.75+18.75 = 52.5

EXTREME OUTLIER

Lower Bound=Q1-3*IQR = 21.25-3(12.5) = 21.25-37.5 = -16.25
Upper Bound=Q3+3*IQR = 33.75+3(12.5) = 33.75+37.5 = 71.25

""""""

data_set8['E_Plug'].replace(120,42,inplace=True)

##CONCATENATION

New_col=pd.read_csv('Data_New.csv')

data_set10=pd.concat([data_set8,New_col],axis=1)

data_set10.info()

data_set10['']
data_set11=pd.get_dummies(data_set10)

data_set11.info()

##NORMALIZATION

from sklearn.preprocessing import minmax_scale,normalize 

data_set12=minmax_scale(data_set11,feature_range=(0,1))

data_set13=normalize(data_set11,norm='l2',axis=0)##axis=0 is for normalizing each feature,axis=1 is for normalizing each sample
## norm='l2' is used for eucledian distance and norm='l1' is used manathan distance

data_set13=pd.DataFrame(data_set13,columns = ['Time','E_Plug','E_Heat','Temp','Price_10','Price_11','Price_12','Price_14','Price_16'
                                            ,'Price_17','Price_18','Price_20','Price_21','Price_22','P/Off_OffPeak','P/Off_Peak'])
