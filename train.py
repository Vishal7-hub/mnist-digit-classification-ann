import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Input
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical


# Load Dataset


(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Data Preprocessing

# Normalize pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-hot encode labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Build ANN Model

model = Sequential([
    Input(shape=(28, 28)),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(10, activation="softmax")
])

# Compile Model

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Display model architecture
model.summary()


# Train Model

history = model.fit(
    x_train,
    y_train,
    validation_split=0.2,
    epochs=5,
    batch_size=32,
    verbose=1
)

print(history.history.keys())
print(history.history["accuracy"])
print(history.history["val_accuracy"])

# Evaluate Model

loss, accuracy = model.evaluate(
    x_test,
    y_test,
    verbose=0
)

print(f"\nTest Accuracy : {accuracy:.4f}")
print(f"Test Loss     : {loss:.4f}")

# Save Trained Model

model.save("model.keras")
print("\nModel saved successfully as 'model.keras'")



# Visualize Training Accuracy

epochs = range(1, len(history.history["accuracy"]) + 1)

plt.figure(figsize=(8, 5))

plt.plot(
    epochs,
    history.history["accuracy"],
    marker="o",
    linewidth=2,
    label="Training Accuracy"
)

plt.plot(
    epochs,
    history.history["val_accuracy"],
    marker="s",
    linewidth=2,
    label="Validation Accuracy"
)

plt.title("Training vs Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.xticks(epochs)
plt.ylim(0.90, 1.00)

plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig("images/training_accuracy.png", dpi=300)

plt.show()
plt.close()



# Visualize Training Loss


plt.figure(figsize=(8, 5))

plt.plot(
    epochs,
    history.history["loss"],
    marker="o",
    linewidth=2,
    label="Training Loss"
)

plt.plot(
    epochs,
    history.history["val_loss"],
    marker="s",
    linewidth=2,
    label="Validation Loss"
)

plt.title("Training vs Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.xticks(epochs)

plt.grid(True)
plt.legend(loc="best")

plt.tight_layout()

plt.savefig(
    "images/training_loss.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()