#missing values (null)
import pandas as pd

data = pd.read_csv("train.csv")
print(data.shape)
print(data.isnull().sum())
#remove columns
#data2= data.drop(columns=["Cabin"])
data.drop(columns=["Cabin"],inplace=True)
#We can use inplace if we dont need the colunm at all
print("After dropping")
print(data.isnull().sum())