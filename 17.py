#this is for row
import pandas as pd

data = pd.read_csv("train.csv")
print(data.shape)

data.dropna(inplace=True)

print("After dropping")

print(data.shape)