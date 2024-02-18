#Categorical Data

import pandas as pd

data = pd.read_csv("lr3.csv")
#lable incodeing
data["Attendance"] = data["Attendance"].map({"Yes":1,"No":0})
