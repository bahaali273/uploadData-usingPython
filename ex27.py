import pandas as pd

data = pd.read_csv("lr3.csv")
data["Attendance"] = data["Attendance"].map({"Yes":1, "No":0})
x = data[["SAT", "Attendance"]]
y = data["GPA"]

print(data.describe())

import statsmodels.api as sm
s = sm.add_constant(x)
res = sm.OLS(y, s).fit()
print(res.summary())


b = res.params[0]
w1 = res.params[1]
w2 = res.params[2]


sat = int(input("Enter SAT score"))
att = input("Yes / No ?")
attendance = 1
if att == "No":
    attendance = 0

print(b + w1 * sat + w2 * attendance)


import matplotlib.pyplot as plt
plt.scatter(data["SAT"], data["GPA"])
yyes = b + w1 * data["SAT"] + w2 * 1
yno = b + w1 * data["SAT"] + w2 * 0
plt.plot(data["SAT"], yyes, c="green")
plt.plot(data["SAT"], yno, c="red")
plt.show()