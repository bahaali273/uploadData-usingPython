import pandas as pd

data =pd.read_csv("wh.csv")

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ["Height"]),
        ('cat',OneHotEncoder(),["Gender"])
    ]
)
x = data[["Height", "Gender"]]
y = data["Weight"]

from sklearn.model_selection import train_test_split

# overfiting => accuresy training > accuracy testing

xtr, xts, ytr, yts = train_test_split(x,y,test_size=0.2)

xtr = preprocessor.fit_transform(xtr)
xts = preprocessor.transform(xts)
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(6,input_dim=3, activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer="adam")

model.fit(xtr, ytr, epochs=80, batch_size=8)

from sklearn.metrics import r2_score
ytr_pred = model.predict(xtr)
print(r2_score(ytr, ytr_pred))

yts_pred = model.predict(xts)
print(r2_score(yts, yts_pred))

example_data =pd.DataFrame({
    'Height':[73],
    'Gender': ['Male']
})

example_data_trans = preprocessor.transform(example_data)
output = model.predict(example_data_trans)
print(output[0][0])