import pandas as pd

data = pd.read_csv("salaries.csv")
x = data["level"]
y = data["salary"]

print(data.describe())

import statsmodels.api as sm
s = sm.add_constant(x)
res = sm.OLS(y, s).fit()
print(res.summary())

b = res.params[0]
w = res.params[1]

import matplotlib.pyplot as plt
plt.scatter(x,y)
yh = b + w * x
plt.plot(x, yh, c="red")
plt.show()