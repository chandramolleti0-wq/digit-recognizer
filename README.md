# Handwritten Digit Recognizer (MNIST)

This is an AI project that recognizes handwritten digits (0–9) using a machine learning model trained on the MNIST dataset.

It uses Flask for the web interface and TensorFlow for the deep learning model.

---

# How to Run the Project

## Step 1: Install Libraries

Run this command:

pip install flask tensorflow numpy opencv-python

---

## Step 2: Train the Model (First Time Only)

Run:

python train.py

This will:
- Load MNIST dataset
- Train AI model
- Save model file (digit_model.h5)

Do this only one time.

---

## Step 3: Run the Web App

Run:

python app.py

---

## Step 4: Open in Browser

Go to:

http://127.0.0.1:5000

---

# Features

- Upload handwritten digit image
- AI predicts digit (0–9)
- Simple web interface
- Fast prediction
- Deep learning model (TensorFlow)

---

# How It Works

1. User uploads image
2. Flask receives image
3. Image is converted to 28x28 grayscale
4. AI model predicts digit
5. Result is shown on screen

---

# Future Improvements

- Draw digit instead of uploading
- Improve accuracy using CNN model
- Deploy online (free hosting)
- Show confidence score

---

# Author

Chandra Sekhar

---

# Note

First run train.py, then run app.py.
