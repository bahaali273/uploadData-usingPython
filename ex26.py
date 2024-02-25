import pandas as pd

data = pd.read_csv("lr1.csv")
x = data["SAT"]
y= data ["GPA"]

print(data.describe())

#OLS (ordinary leatst square)

import statsmodels.api as sm
s = sm.add_constant(x)
result = sm.OLS(y, s).fit()
print(result.summary())
#yh =  0.2750 + 0.0017 * x ( x for example what is the result for the student result in SAT program to predect his marks in the university)

b = result.params[0]
w = result.params[1]

sat =int(input("Enter SAT score"))
print(b + w * sat)

import matplotlib.pyplot as plt
plt.scatter(x,y)
yh = b + w * x
plt.plot(x, yh, c="red")
plt.show()