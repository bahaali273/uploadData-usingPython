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

#data["result"]=cls_result => to add this to the table
"""
plt.scatter(data["SAT"], data["Admitted"])
plt.scatter(data["SAT"], cls_result, c= "red")
plt.show()
"""
#Confusion Matrix => comper predected and Actual data
cm = res.pred_table()
print(cm)
#168 the number of samples
cmv = cm[0][0] + cm[1][1]
print("CMV =")
print(cmv/168)

#Single Prediction

sat = int(input("Enter SAT score"))
gen =input("Male / Female ?")
gender =1
if gen =="Male":
    gender =0

sample = pd.DataFrame({'const':1,'SAT':[sat], 'Gender':[gender]})
sample=sample[["const","SAT","Gender"]]
admt =res.predict(sample)
print(admt)

if admt[0]> 0.59:
    print("Accepted")
else:
    print("Rejected")


# Learning Methods: Supervised => (input + output) && Unsupervised => (input)