# Descripttive Analysis => how to discripe your data
# Analysis(old and Current) vs Analytics (Prediction)
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


#Visualization
import matplotlib.pyplot as plt
import seaborn as sns

sns.heatmap(cor_matrix, annot=True)
plt.title("Correlation Matrix")
plt.show()

sns.pairplot(data)
plt.show()