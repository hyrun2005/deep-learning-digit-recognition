# 🖊️ Handwritten Digit Recognition Web App

This is a **Flask-based web application** that recognizes handwritten digits using a **CNN trained on MNIST**. Users can draw a digit on an HTML5 canvas, and the model predicts the number in real-time.


---

## 🚀 Features
- Draw a digit on the **web canvas**
- Uses a **trained CNN model** for digit recognition
- Flask API processes images and returns predictions
- Simple **frontend with real-time predictions**
- **Easy setup** with minimal dependencies

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/hyrun2005/deep-learning-digit-recognition.git
cd deep-learning-digit-recognition
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App
```bash
python app.py
```
- Open **http://127.0.0.1:5000/** in your browser.

---

## 🎨 How to Use?
1️⃣ Open the web app.  
2️⃣ Draw a digit on the canvas.  
3️⃣ Click **"Predict"**, and the model will identify the digit.  

---

## 🔬 Model Details
- **Dataset**: MNIST (60,000 training, 10,000 testing images).
- **Architecture**: Convolutional Neural Network (CNN) with:
  - Convolutional & Pooling layers
  - Fully connected layers
  - Softmax activation for digit classification

---

## 👤 Author
- **Yurii Hyrun**
- [GitHub](https://github.com/hyrun2005)
- [LinkedIn](https://www.linkedin.com/in/yurii-hyrun-897b9b277/)

---

## 📝 License
This project is open-source under the **MIT License**.

