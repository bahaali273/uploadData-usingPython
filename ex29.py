# Unsupervised => there is no output
import pandas as pd

data = pd.read_csv("cluster1.csv")

x = data[["Latitude","Longitude"]]

from sklearn.cluster import KMeans
km = KMeans(3)
km.fit(x)
result = km.fit_predict(x)
print(result)

data["cluster"] = result
print(data)


import matplotlib.pyplot as plt
plt.scatter(data["Longitude"], data["Latitude"], c=result)
plt.show()

#wcss => Within-Cluster Sum of Square
wcss =[]
for i in range(1, 7):
    km = KMeans(i)
    km.fit(x)
    wcss.append(km.inertia_)
groups = range(1,7)
plt.plot(groups,wcss)
plt.show()