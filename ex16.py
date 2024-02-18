import pandas as pd

data = pd.read_csv("train.csv")
print(data.isnull().sum())
#to print the avg of the age
avg_age = data["Age"].mean()
print((avg_age))

import numpy as np
# we need numpy to count null val
#in this ex we need to change anyone has 25 age to 29 or null to 29
#data["Age"].replace(25,29, inplace=True)
data["Age"].replace(np.NAN,int(avg_age), inplace=True)
print("-------------------------")
print(data.isnull().sum())