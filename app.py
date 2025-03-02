from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import cv2
import base64
import io
from PIL import Image

app = Flask(__name__)

# Load trained CNN model
model = tf.keras.models.load_model("digit_prediction.keras")

# Function to process base64 image from canvas
def preprocess_canvas_image(image_data):
    # Decode base64 to image
    image_data = image_data.split(",")[1]
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes)).convert("L")

    # Resize and apply padding
    image = np.array(image)

    if np.mean(image) > 127:
        image = cv2.bitwise_not(image)

    # Find bounding box of digit and crop it
    coords = cv2.findNonZero(image)
    x, y, w, h = cv2.boundingRect(coords)
    image = image[y:y + h, x:x + w]

    # Resize to 20x20 while maintaining aspect ratio
    rows, cols = image.shape
    factor = 20.0 / max(rows, cols)
    image = cv2.resize(image, (int(cols * factor), int(rows * factor)))

    # Create a 28x28 canvas and place the digit in the center
    new_image = np.zeros((28, 28), dtype=np.uint8)
    x_offset = (28 - image.shape[1]) // 2
    y_offset = (28 - image.shape[0]) // 2
    new_image[y_offset:y_offset + image.shape[0], x_offset:x_offset + image.shape[1]] = image

    # Normalize and reshape for model input
    new_image = new_image.astype("float32") / 255.0
    new_image = new_image.reshape(1, 28, 28, 1)

    return new_image


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if "image" not in data:
        return jsonify({"error": "No image data"}), 400

    image = preprocess_canvas_image(data["image"])

    # Predict using model
    prediction = model.predict(image)
    predicted_digit = np.argmax(prediction)

    return jsonify({"digit": int(predicted_digit)})

if __name__ == "__main__":
    app.run(debug=True)
