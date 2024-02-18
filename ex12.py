#read and drow from csv file
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("lr1.csv")
x = data["SAT"]
y = data["GPA"]

plt.scatter(x,y)
plt.show()