from flask import Flask, render_template, request
import numpy as np
import cv2
from model import model

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]

    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28,28))
    img = img / 255.0
    img = img.reshape(1,28,28)

    prediction = model.predict(img)
    digit = np.argmax(prediction)

    return f"Predicted Digit: {digit}"

if __name__ == "__main__":
    app.run(debug=True)
