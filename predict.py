import random

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

model = tf.keras.models.load_model("model.keras")

(_, _), (x_test, y_test) = mnist.load_data()
x_test = x_test / 255.0

index = random.randint(0, len(x_test) - 1)
image = x_test[index]
actual_label = y_test[index]

print(image.shape)
image = np.expand_dims(image, axis=0)

prediction = model.predict(image)
predicted_label = np.argmax(prediction)

print("Actual Label   :", actual_label)
print("Predicted Label:", predicted_label)

plt.imshow(image[0], cmap="gray")

plt.title(
    f"Actual: {actual_label} | Predicted: {predicted_label}"
)

plt.axis("off")

plt.show()

