
from sklearn.datasets import load_digits

digits = load_digits()
x = digits.data
y = digits.target

import matplotlib.pyplot as plt
plt.imshow(x[1450].reshape(8,8))
plt.show()
print(y[1450])

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(16, input_shape=(64,),activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(10, activation='softmax'))  # output => 10
#softmax => multipal classifcation
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])


from keras.utils import to_categorical
yc = to_categorical(y)

#Learning Curve
from sklearn.model_selection import train_test_split
xtr, xts, ytr, yts = train_test_split(x, yc, test_size=0.3)

#train_sizes= [300, 600, 900, 1257]

import numpy as np 
train_sizes = (len(xtr) * np.linspace(0.2,0.9999,4)).astype(int)

iw = model.get_weights() 
acc_scores =[]

for i in train_sizes:
    xtr2, _, ytr2, _ = train_test_split(xtr, ytr, train_size=i)
    model.fit(xtr2, ytr2, epochs=250, verbose=0)
    acc = model.evaluate(xts, yts)
    acc_scores.append(acc[1])
    model.set_weights(iw)
    print(i)

"""""
from sklearn.datasets import load_digits
digits = load_digits()
x = digits.data
y = digits.target

import matplotlib.pyplot as plt
plt.imshow(x[1278].reshape(8,8))
plt.show()

print(y[1278])

# Create Neural Network
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
model = Sequential()
model.add(Dense(16, input_shape=(64,), activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

yc = to_categorical(y)

# Learning Curve (samples=1797, training=1257, testing=540)
from sklearn.model_selection import train_test_split
xtr, xts, ytr, yts = train_test_split(x, yc, test_size=0.3)

import numpy as np
train_sizes = (len(xtr) * np.linspace(0.2, 0.9999, 4)).astype(int)
print(train_sizes)

acc_scores = []
iw = model.get_weights()

for i in train_sizes:
    xtr2, _, ytr2, _ = train_test_split(xtr, ytr, train_size=i)
    model.fit(xtr2, ytr2, epochs=300, verbose=0)
    acc = model.evaluate(xts, yts)
    acc_scores.append(acc[1])
    model.set_weights(iw)
    print(i)
"""""