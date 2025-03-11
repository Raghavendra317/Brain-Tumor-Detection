import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Load the trained model
MODEL_PATH = "model/brain_tumor_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Define class labels
class_labels = {0: "Glioma", 1: "Meningioma", 2: "No Tumor", 3: "Pituitary"}

# Function to preprocess the image
def preprocess_image(image):
    image = image.convert("RGB")  # Ensure 3 channels
    image = image.resize((150, 150))  # Resize to match model input
    image_array = np.array(image) / 255.0  # Normalize
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array

# Streamlit UI
st.title("🧠 Brain Tumor Detection")
st.write("Upload an MRI scan to classify if it has a brain tumor.")

# File uploader
uploaded_file = st.file_uploader("Choose an MRI scan...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess and predict
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction)
    confidence = round(100 * np.max(prediction), 2)

    # Display result
    st.success(f"Prediction: **{class_labels[predicted_class]}**")
    st.info(f"Confidence: {confidence}%")
