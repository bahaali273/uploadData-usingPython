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
# (100 - accuracy "Pseudo R-squ") / 2 => ex. 100 -82 =18 /2 = 9 => after this we have to add this number to 50% and minimize it from 50%
import numpy as np
np.set_printoptions(formatter={'float':lambda x:"{0:0.3f}".format(x)})
cls_result = res.predict()
print(cls_result)

# to change this accuracy number
print(cls_result > 0.59)

plt.scatter(data["SAT"], data["Admitted"])
plt.show()