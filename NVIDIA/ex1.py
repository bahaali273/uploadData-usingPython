import tensorflow as tf

tf.config.list_physical_devices('GPU')
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (valid_images, valid_labels) = fashion_mnist.load_data()

import matplotlib.pyplot as plt
 # The question number to study with. Feel free to change up to 59999.
data_idx =42
plt.figure()
plt.imshow(train_images[data_idx], cmap='gray')
plt.colorbar()
plt.grid(False)
plt.show()

train_labels[data_idx]


# 28 lists with 28 values each

print(valid_images[data_idx] )

number_of_classes = train_labels.max() + 1
print(number_of_classes)

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(number_of_classes)
])
print(model.summary())

image_height = 28
image_width = 28

number_of_weights = image_height * image_width * number_of_classes
print(number_of_weights)

tf.keras.utils.plot_model(model, show_shapes=True)
print(model)

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(
    train_images,
    train_labels,
    epochs=5,
    verbose=True,
    validation_data=(valid_images, valid_labels)
)

model.predict(train_images[0:10])

data_idx = 8675 # The question number to study with. Feel free to change up to 59999.

plt.figure()
plt.imshow(train_images[data_idx], cmap='gray')
plt.colorbar()
plt.grid(False)
plt.show()

x_values = range(number_of_classes)
plt.figure()
plt.bar(x_values, model.predict(train_images[data_idx:data_idx+1]).flatten())
plt.xticks(range(10))
plt.show()

print("correct answer:", train_labels[data_idx])
