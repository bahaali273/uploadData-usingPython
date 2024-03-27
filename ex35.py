#single and multiple classification
# Single => Binary Crossentropy => sigmoid
# Multiple => Categorical Crossentropy

import pandas as pd
import numpy as np
import scikeras

data=pd.read_csv("visit.csv")
x = data[["Time"]]
y = data[["Buy"]]

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

#Cross Validation (to find exact accuracy)
# = Folds(4) => 100/4 =25  # Wrapper

from scikeras.wrappers import KerasClassifier
def get_model():
    model = Sequential()
    model.add(Dense(1, input_shape=(1,), activation='sigmoid'))
    model.compile(Adam(learning_rate=0.99), loss="binary_crossentropy",
                  metrics=["accuracy"])
    return model

wrapper_model =KerasClassifier(build_fn=get_model,epochs=25)
# KFold => how many time you need to run it
# cross_val_score => accuricy
from sklearn.model_selection import KFold, cross_val_score

KF = KFold(4)
acc = cross_val_score(wrapper_model, x,y, cv=KF)
print(acc)
print(acc.mean())



