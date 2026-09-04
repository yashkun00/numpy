# 🧠 NumPy + TensorFlow Neural Network Prediction

A beginner-friendly Deep Learning project that demonstrates how **NumPy** can be used to prepare numerical data and **TensorFlow/Keras** can be used to train a simple neural network for prediction.

This project focuses on understanding the basic workflow of a machine learning model — from creating data to training the model and generating predictions.

---

## 📌 Project Overview

The project uses NumPy arrays to create a small dataset containing input and output values.

A simple **Dense Neural Network** is then created using TensorFlow/Keras. The model learns the relationship between the input and output values during training.

After training, a new value is passed to the model to generate a prediction.

---

## 🧠 How It Works

The basic workflow is:

```text
NumPy Data
    ↓
Input & Output Arrays
    ↓
Build Neural Network
    ↓
Compile Model
    ↓
Train Model
    ↓
Make Prediction
```

---

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **TensorFlow**
* **Keras**

---

## 📦 Installation

Install the required libraries:

```bash
pip install numpy tensorflow
```

---

## 📊 Dataset

The training data is created using NumPy:

```python
import numpy as np

x = np.array([[1], [1], [3], [4]])
y = np.array([[2], [4], [6], [8]])
```

Here, `x` represents the input data and `y` represents the expected output.

The neural network attempts to learn the relationship between these values.

---

## 🏗️ Model Architecture

The project uses a simple Keras Sequential model with a single Dense layer.

```python
model = Sequential([
    Dense(1, input_shape=(1,))
])
```

The model contains:

* Input layer
* One Dense layer
* One output neuron

This simple architecture is useful for understanding the fundamentals of neural network prediction.

---

## ⚙️ Model Compilation

The model is compiled using:

```python
model.compile(
    optimizer='sgd',
    loss='mse'
)
```

### Optimizer

**SGD (Stochastic Gradient Descent)** is used to update the model's weights during training.

### Loss Function

**MSE (Mean Squared Error)** measures the difference between the predicted values and the actual values.

---

## 🚀 Training

The model is trained using:

```python
model.fit(
    x,
    y,
    epochs=10,
    verbose=0
)
```

The model goes through the training dataset multiple times and gradually adjusts its parameters to improve its predictions.

---

## 🔮 Prediction

After training, a new value can be passed to the model:

```python
prediction = model.predict(np.array([[6]]))
print(prediction)
```

The model uses what it learned during training to estimate the corresponding output.

---

## 📁 Project Structure

```text
📦 NumPy-TensorFlow-Prediction
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🎯 Learning Outcomes

This project helps demonstrate the fundamentals of:

* Creating NumPy arrays
* Preparing training data
* Building a neural network
* Using Keras Sequential models
* Understanding Dense layers
* Compiling a model
* Using SGD optimization
* Understanding MSE loss
* Training a neural network
* Making predictions with TensorFlow

---

## 🔧 Future Improvements

This basic project can be extended by:

* Adding more training data
* Increasing the number of neurons
* Adding additional layers
* Experimenting with different optimizers
* Increasing the number of epochs
* Visualizing training loss
* Testing the model with unseen data

---

## 👨‍💻 Author

**Yash**

⭐ If you found this project useful, consider giving the repository a star.

