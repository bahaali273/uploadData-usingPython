import pandas as pd
import sklearn.preprocessing as pre
data = pd.read_csv("cluster4.csv")
x = pre.scale(data[["Satisfaction", "Loyalty"]])


from sklearn.cluster import KMeans
km = KMeans(4)
km.fit(x)
result = km.fit_predict(x)

import matplotlib.pyplot as plt
plt.scatter(data["Satisfaction"], data["Loyalty"], c=result)
plt.show()