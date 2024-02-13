import pandas as pd
# option + shift + E to run line by line
data = pd.read_csv("cluster1.csv")
print(data.head(3))
print(data["Country"])
print(data[["Country","Language"]])

data["Population"] = [200, 80, 55, 100, 60, 75]
print(data)

data.to_csv("newFilecluster.csv")
