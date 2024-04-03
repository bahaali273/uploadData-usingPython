# 4 input and one output length and width for sepal and petal for flower,
# the output should be the flower type
import pandas as pd

data = pd.read_csv("iris.csv")       
# new strategy: if I have too many columns like 20 and the output in the end 21 i have to use this way
# mean give me all the columns except [species] and i can add more if i want
x = data.drop(columns=["species"])
y= data["species"]


#Now i have to covert text to numbers

target_name = data["species"].unique()
#unique() => data without repation
print(target_name)

# this is label wa to convert it (not recommended) => y= data["species"].map({'setosa':1, 'versicolor':2, 'virginica':3})
# target_numbers ={n:i for i, n in enumerate(target_names)}// this is loop way insted to write all attributes
y= data["species"].map({'setosa':0, 'versicolor':1, 'virginica':2})
#convert it to (One hot) way
from keras.utils import to_categorical
yc =to_categorical(y) # => one hot encoding

#---------PreProcessing for data (data clensing)-----------
#---------now we will staer with AI Model-----------------
#--------- Multiple Classification--------------------

#sigmoid => for single classification
#softmax =>for multiple Classification
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

model =Sequential()
model.add(Dense(3,input_shape=(4,),activation='softmax'))
model.compile(Adam(learning_rate=0.99),loss="categorical_crossentropy",
              metrics=["accuracy"])
model.fit(x,yc, epochs=40)

# sl => sepal_length , sw => sepal-width , pl=> petal lenght ,pw=> petal width
sl = float(input("Enter sepal length"))
sw = float(input("Enter sepal width"))
pl = float(input("Enter petal length"))
pw = float(input("Enter petal length"))


# do predict
import numpy as np
xt = np.array([[sl,sw,pl,pw]])
yt= model.predict(xt)

spc= np.argmax(yt)
print(spc)

spc_numbers ={i:n for i, n in enumerate(target_name)}
print(spc_numbers[spc])