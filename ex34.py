#build model from zero

import pandas as pd
data = pd.read_csv("wh.csv")
x= data["Height"]
y= data["Weight"]

from keras.models import Sequential
# Sequential from input to output one to another like neural network
from keras.layers import Dense
#Dense to give output from Input
from keras.optimizers import Adam

# We will start with Sequential single lain one input and output

model = Sequential()
model.add(Dense(1, input_shape=(1,))) # 1 output and 1 input
model.compile(Adam(learning_rate=0.5), loss="mean_squared_error")
# epochs => how many times i need to train the model
model.fit(x, y,epochs=100)

#comper result after and befor
yp = model.predict(x)
#to find the accuricy
import sklearn.metrics as mtr
print(mtr.r2_score(y, yp))

import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.plot(x,yp, c="red")
plt.show()


#Single prediction

