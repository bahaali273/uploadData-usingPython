# Descripttive Analysis => how to discripe your data

import pandas as pd

data = pd.read_csv("house.csv")
# General information about your file #   Column  Non-Null Count  Dtype
print(data.info())
#data statistics
print("data statistics")
print(data.describe())