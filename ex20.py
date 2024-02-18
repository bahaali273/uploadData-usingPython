#Scaling
# we need to download pip install scikit-learn
import pandas as pd
data= pd.read_csv("house.csv")

import sklearn.preprocessing as pre

data2 = pre.scale(data)