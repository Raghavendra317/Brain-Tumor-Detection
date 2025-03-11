# 🧠 Brain Tumor Detection - Deep Learning  
![Brain Tumor Detection](https://user-images.githubusercontent.com/your-image-url)  

### 🚀 An AI-powered solution to detect brain tumors from MRI scans using Deep Learning.  

---

## 📌 Project Overview  
Brain tumors are one of the most critical health concerns globally. Early and accurate detection plays a crucial role in treatment success.  
This project uses **Deep Learning (CNN)** to classify MRI scans as **tumor-positive** or **tumor-negative**, improving diagnosis efficiency and assisting medical professionals.  

---

## 🖥️ Demo  
🔗 **Live Deployment:** [Streamlit App](https://your-streamlit-app-url)  

Upload an MRI scan and let the model predict whether a tumor is present.  

---
## ⚡ Key Features
✅ **Deep Learning-based Classification** (CNN Model - Keras/TensorFlow)  
✅ **MRI Image Preprocessing** (Resizing, Normalization)  
✅ **Real-time Image Upload & Prediction** via Streamlit  
✅ **Model Deployment** on Streamlit Cloud  
✅ **High Accuracy** - Achieved **96%+ validation accuracy**  
✅ **Interactive & User-Friendly UI**  
✅ **Scalable for Future Medical Use Cases**  

---

## 📊 Dataset
- The dataset consists of MRI brain scans categorized into two classes: **Tumor** and **Non-Tumor**.  
- Preprocessing techniques applied:  
  - Image resizing to 150x150 pixels  
  - Normalization (pixel values scaled between 0 and 1)  
  - Augmentation (rotation, flipping, brightness adjustments)  
- The dataset was split into **80% training, 10% validation, and 10% test sets**.  

---

## 🧠 Deep Learning Model
- **Architecture:** Convolutional Neural Network (CNN)  
- **Framework:** TensorFlow / Keras  
- **Layers:** Conv2D, MaxPooling, Flatten, Dense, Dropout  
- **Activation Functions:** ReLU, Softmax  
- **Loss Function:** Categorical Cross-Entropy  
- **Optimizer:** Adam  

### 📈 Model Performance  
- **Training Accuracy:** 98.7%  
- **Validation Accuracy:** 96.2%  
- **Loss:** 0.09  

**Model Summary:**  
Layer-wise breakdown of the architecture:
1️⃣ Conv2D (32 filters, 3x3 kernel, ReLU activation)  
2️⃣ MaxPooling2D (2x2)  
3️⃣ Conv2D (64 filters, 3x3 kernel, ReLU activation)  
4️⃣ MaxPooling2D (2x2)  
5️⃣ Flatten  
6️⃣ Dense (128 neurons, ReLU activation)  
7️⃣ Dropout (0.5)  
8️⃣ Output Layer (Softmax activation)  

---

## 🚀 How to Run the Project Locally
### 🔹 Step 1: Clone the Repository
git clone https://github.com/Raghavendra317/Brain-Tumor-Detection.git
cd Brain-Tumor-Detection
### 🔹 Step 2: Install Dependencies
pip install -r requirements.txt
### 🔹 Step 3: Run the Streamlit App
streamlit run app.py

---

## 📸 Screenshots
### 🔹 Web App Interface  
![App Screenshot](https://user-images.githubusercontent.com/your-image-url)  

### 🔹 Sample Predictions  
![Predictions Screenshot](https://user-images.githubusercontent.com/your-image-url)  

---

## 📜 License
This project is licensed under the **MIT License** – you are free to modify and distribute it.  

---

## 📞 Contact
👤 **Raghavendra S**  
📧 **[raaghu07012003@gmail.com]**  
🔗 **[LinkedIn](www.linkedin.com/in/raghavendra-s-270857314)**  
🔗 **[GitHub](https://github.com/Raghavendra317)**  

--

**✨ If you found this project useful, please ⭐ star the repository! ✨**  

🚀 **Happy Coding!** 🚀  


