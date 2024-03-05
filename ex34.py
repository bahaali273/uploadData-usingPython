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
w, b =model.get_weights()
#retern all (W) and in the end retern (b)
h=float(input("Enter height"))
print(b+ w* h)

#Over-fitting
# 1- Train test Split (10000 samples = Training (80% => 8000) + Testing (20% =>2000)
# 2- Train the model (8000)
# 3- Calculate training accuracy
# 4- Predict (2000)
# 5- Calculate testing accuracy
# 6- if the training accuracy > testing accuracy (Over-fitting)
#1
from sklearn.model_selection import train_test_split
xtr, xts, ytr, yts = train_test_split(x,y, test_size=0.2)
#x (xtr),y (ytr)training 8000
#x (xts), y (yts) Testing 2000
model.fit(xtr, ytr, epochs=100)

#3
ytrp = model.predict(xtr)
ytsp = model.predict(xts)
print(mtr.r2_score(ytr,ytrp))
print(mtr.r2_score(yts, ytsp))