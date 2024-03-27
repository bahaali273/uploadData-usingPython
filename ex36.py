# 4 input and one output length and width for sepal and petal for flower,
# the output should be the flower type
import pandas as pd

data = pd.read_csv("iris.csv")
# new strategy: if I have too many columns like 20 and the output in the end 21 i have to use this way
x = data