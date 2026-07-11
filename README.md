#  Handwritten Digit Classification using Artificial Neural Network (ANN)

> A Deep Learning project that classifies handwritten digits (0–9) using an Artificial Neural Network (ANN) built with TensorFlow and Keras on the MNIST dataset.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange?logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-NeuralNetwork-red?logo=keras)
![License](https://img.shields.io/badge/License-MIT-green)

---

#  Project Overview

This project demonstrates the complete workflow of building an Artificial Neural Network (ANN) for handwritten digit recognition using the MNIST dataset.

The project covers every major step of a Machine Learning pipeline—from data preprocessing and model training to evaluation, visualization, model persistence, and inference.

Rather than focusing only on achieving high accuracy, this project emphasizes clean project structure, reproducibility, and maintainable code, following professional Git and GitHub practices.

---

#  Features

-  MNIST dataset preprocessing
-  Image normalization
-  One-hot encoding of labels
-  Artificial Neural Network (ANN) implementation
-  Model training with validation split
-  Performance evaluation on unseen test data
-  Model persistence using TensorFlow
-  Training & Validation Accuracy visualization
-  Training & Validation Loss visualization
-  Random digit prediction using saved model
-  Clean project structure
-  Version-controlled development using Git

---

#  Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| TensorFlow | Deep Learning Framework |
| Keras | Neural Network API |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Git & GitHub | Version Control |

---

#  Project Structure

```
mnist-digit-classification-ann/
│
├── images/
│   ├── training_accuracy.png
│   └── training_loss.png
│
├── train.py
├── predict.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Dataset

The project uses the famous **MNIST Handwritten Digits Dataset**.

| Property | Value |
|----------|-------|
| Training Images | 60,000 |
| Test Images | 10,000 |
| Image Size | 28 × 28 |
| Classes | 10 (Digits 0–9) |

---

#  Model Architecture

```
Input (28 × 28)

        │

     Flatten

        │

 Dense (128, ReLU)

        │

 Dense (10, Softmax)

        │

Predicted Digit
```

---

#  Training Configuration

| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Epochs | 5 |
| Batch Size | 32 |
| Validation Split | 20% |

---

#  Model Performance

| Metric | Value |
|--------|-------|
| Test Accuracy | **97.6%** |
| Test Loss | **0.0797** |

---

#  Training Accuracy



![Training Accuracy](images/training_accuracy.png)

---

#  Training Loss

![Training Loss](images/training_loss.png)

---

#  Sample Prediction

The trained model randomly selects an image from the MNIST test dataset and predicts the handwritten digit.

Example Output

```
Actual Label   : 5
Predicted Label: 5
```

---

#  Installation

Clone the repository

```bash
git clone https://github.com/Vishal7-hub/mnist-digit-classification-ann.git
```

Move into the project directory

```bash
cd mnist-digit-classification-ann
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

#  Run the Project

### Train the Model

```bash
python train.py
```

### Predict a Digit

```bash
python predict.py
```

---

#  Note

The trained model (`model.keras`) is intentionally excluded from the repository using `.gitignore` to keep the repository lightweight.

To generate the trained model locally, simply run:

```bash
python train.py
```

This will automatically create the trained model required for inference.

---

#  Learning Outcomes

Through this project, I gained hands-on experience with:

- Neural Network Fundamentals
- Data Preprocessing
- Image Normalization
- Model Training & Validation
- Model Evaluation
- TensorFlow/Keras Workflow
- Model Saving & Loading
- Inference Pipeline
- Performance Visualization
- Git & GitHub Best Practices

---

#  Future Improvements

- Convolutional Neural Network (CNN)
- Hyperparameter Tuning
- Streamlit Web Application
- Custom Handwritten Image Prediction
- Model Deployment
- Confusion Matrix & Classification Report

---

#  Author

**Vishal Kumar Roy**

Aspiring Machine Learning Engineer | Data Science Enthusiast



---

##  If you found this project useful, consider giving it a Star!