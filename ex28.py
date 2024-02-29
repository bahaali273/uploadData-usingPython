#Example for A or B ? (Classification) => single or Multiple

# function called Logit for Classification
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("logr1.csv")
data["Admitted"] = data["Admitted"].map({"Yes":1, "No":0})
data["Gender"] = data["Gender"].map({"Female":1, "Male":0})
x = data[["SAT","Gender"]]
y = data["Admitted"]

import statsmodels.api as sm
s = sm.add_constant(x)
res = sm.Logit(y, s).fit()
print(res.summary())


plt.scatter(data["SAT"], data["Admitted"])
plt.show()