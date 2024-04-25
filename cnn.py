from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D, MaxPool2D, Flatten, Dense

model = Sequential()
model.add(Convolution2D(32,3,3, input_shape=(64,64,3),activation='relu'))#8 or 64 width , 8 or 64linght, 3-> 3 chanale colored
# 32 how many featuers between cat and dogs


# Now We need to do Max Pooling
model.add(MaxPool2D(2,2))
model.add(Flatten())

#Nural Network
model.add(Dense(128,activation='relu'))
model.add(Dense(128,activation='relu'))
model.add(Dense(1,activation='sigmoid')) # 1 => singal, 2 => multipal (softmax)
model.compile(loss="binary_crossentropy", optimizer="adam",matrics=["accuracy"])

# img (data) preprocessing
from tensorflow.keras.preprocessing.image import ImageDataGenerator

tr_datagen = ImageDataGenerator(rescale=1/255, horizontal_flip=True, zoom_range=0.2,shear_range=0.2)

ts_datagen = ImageDataGenerator(rescale=1/255)

# Data Augmentation => filter image and do deffernt styles and create copy of them

tr_dataset = tr_datagen.flow_from_directory('dataset/training_set', target_size=(64,64), class_mode="binary", batch_size=32) # this is for Training /64, 64 the same number in the above/ it could be binary => singl clasification or category => multibal classification
ts_dataset =ts_datagen.flow_from_directory('dataset/training_set', target_size=(64,64), class_mode="binary", batch_size=32)# this one for testing

# Training
model.fit(tr_dataset, step_pre_epoch=int(4000/32),epoch=100,
          validation_data=ts_dataset, validation_steps=int(1000/32))


