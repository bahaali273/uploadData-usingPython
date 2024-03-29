# 4 input and one output length and width for sepal and petal for flower,
# the output should be the flower type
import pandas as pd

data = pd.read_csv("iris.csv")
# new strategy: if I have too many columns like 20 and the output in the end 21 i have to use this way
# mean give me all the columns except [species] and i can add more if i want
x = data.drop(columns=["species"])
y= data["species"]


#Now i have to covert text to numbers

target_name = data["species"].unique()
#unique() => data without repation
print(target_name)

y= data["species"].map({'setosa':1, 'versicolor':2, 'virginica':3})