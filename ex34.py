#bild model from zero

import pandas as pd
data = pd.read_csv("wh.csv")
x= data["Height"]
y= data["weight"]

from keras.models import Sequential
# Sequential from input to output one to another
from keras.layers import Dense
#Dense to give output from Input
from keras.optimizers import Adam

# We will start with Sequential single lain one input and output

model = Sequential()
model.add(Dense(1, input_shape=(128,128,20))) # 1 output and 1 input

