import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#Create the dataframe using the 
filename = './linearregression/data1.csv'
with open(filename) as f:
    content = f.readlines()

df = pd.read_csv(filename)
df.reset_index(inplace=True)
model = LinearRegression()
model.fit(df[['hours']],df.testscore)
pred = model.predict(df[['hours']])
print ("pred : ", pred)
print ("actual : ", df.testscore)

rmse = mean_squared_error(df.testscore, pred)
print ("Coefficient: ", model.coef_)
print ("Intercept: ", model.intercept_)
print ("Root Mean Square error: ", rmse)
print (model.summary())
print ("Standard error of estimate: ", )

df1 = pd.read_csv(filename)
df1.reset_index(inplace=True)
print(df1)
