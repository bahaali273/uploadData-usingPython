#single and multiple classification
# Single => Binary Crossentropy => sigmoid
# Multiple => Categorical Crossentropy

import pandas as pd

data=pd.read_csv("visit.csv")
x = data["Time"]
y = data["Buy"]

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

model =Sequential()
model.add(Dense(1,input_shape=(1,),activation='sigmoid'))
model.compile(Adam(learning_rate=0.99),loss="binary_crossentropy",
              metrics=["accuracy"])

model.fit(x, y,epochs=25)

yp = model.predict(x)
ypc =yp > 0.5
#accurecy
from sklearn.metrics import accuracy_score, confusion_matrix
print(accuracy_score(y,ypc))

#confusion matrix
print(confusion_matrix(y, ypc))

#Cross Validation
