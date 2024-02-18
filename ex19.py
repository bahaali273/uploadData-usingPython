#One Hot incoding

import pandas as pd

data = pd.read_csv("iris.csv")
#get_dummies => change to T and F
one_hot = pd.get_dummies(data["species"])
# to joiun this one_hot with Data files
data = data.join(one_hot)
# to delete column becase we don't need char only numbers
data= data.drop(columns=["species"])
