import streamlit as st
import tensorflow as tf
import numpy as np
import urllib.request
import os
from PIL import Image

# Title
st.title("🧠 Brain Tumor Detection App")
st.write("Upload an MRI scan to predict whether the brain has a tumor.")

# Define model path and GitHub release URL
MODEL_PATH = "brain_tumor_model.keras"
MODEL_URL = "https://github.com/Raghavendra317/Brain-Tumor-Detection/releases/download/v1.0/brain_tumor_model.keras"

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
    prediction = model.predict(processed_image)[0][0]

    # Display Result
    st.subheader("🔍 Prediction:")
    if prediction > 0.5:
        st.error("🚨 Brain Tumor Detected!")
    else:
        st.success("✅ No Brain Tumor Detected!")
