import pandas as pd

data = pd.read_csv("salaries.csv")

x = data[["level"]]
y = data[["salary"]]
# we use double [[]] 
from sklearn.preprocessing import PolynomialFeatures

poly= PolynomialFeatures(degree=3)
xp =poly.fit_transform(x)

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(xp, y)
yh =linreg.predict(xp)

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.plot(x,yh, c= "red")
plt.show()