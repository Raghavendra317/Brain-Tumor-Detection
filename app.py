import streamlit as st
import tensorflow as tf
import numpy as np
import urllib.request
import os
from PIL import Image

# Title
st.title("🧠 Brain Tumor Classification App")
st.write("Upload an MRI scan to classify the type of brain tumor.")

# Define model path and GitHub release URL
MODEL_PATH = "brain_tumor_model.keras"
MODEL_URL = "https://github.com/Raghavendra317/Brain-Tumor-Detection/releases/download/v1.0/brain_tumor_model.keras"

# Class Labels
CLASS_NAMES = ["Glioma Tumor", "Meningioma Tumor", "Pituitary Tumor", "No Tumor"]

# Function to download model if not present
def download_model():
    if not os.path.exists(MODEL_PATH):
        st.warning("Downloading the model... This may take a while.")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        st.success("Model downloaded successfully!")

# Download model if missing
download_model()

# Load the model
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    st.success("✅ Model Loaded Successfully!")
except Exception as e:
    st.error(f"⚠️ Error loading model: {e}")
    st.stop()

# Function to preprocess image
def preprocess_image(image):
    image = image.resize((150, 150))  # Resize to match model input size
    image = np.array(image) / 255.0   # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Upload image
uploaded_file = st.file_uploader("📤 Upload an MRI Scan", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Uploaded Image", use_column_width=True)
    
    # Preprocess image
    processed_image = preprocess_image(image)

    # Make prediction
    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction)  # Get the class index
    confidence = np.max(prediction) * 100    # Get confidence score

    # Display Result
    st.subheader("🔍 Classification Result:")
    st.write(f"**Predicted Class:** {CLASS_NAMES[predicted_class]}")
    st.write(f"**Confidence:** {confidence:.2f}%")
    
    # Show warning if confidence is low
    if confidence < 60:
        st.warning("⚠️ The model is uncertain about this prediction. Consider rechecking with another scan.")
