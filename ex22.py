# Descripttive Analysis => how to discripe your data

import pandas as pd

data = pd.read_csv("house.csv")
# General information about your file #   Column  Non-Null Count  Dtype
print("Data Info")
print(data.info())
#data statistics
print("data statistics")
print(data.describe())

#Correlation => relation between different columns and it will be between (-1 to 1)

cor_matrix = data.corr()
print("Correlation Matrix : ")
print(cor_matrix)


