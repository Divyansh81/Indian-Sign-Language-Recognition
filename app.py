import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Set page configuration
st.set_page_config(page_title="ISL Recognition", page_icon="🤟", layout="wide")

# Custom CSS for a more premium look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .title-text {
        text-align: center;
        color: #1E3A8A;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .subtitle-text {
        text-align: center;
        color: #4B5563;
        margin-bottom: 2rem;
    }
    .prediction-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        border: 2px solid #E5E7EB;
    }
    </style>
""", unsafe_allow_html=True)

# Load Model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('isl_recognition_model.h5')
    return model

with st.spinner("Loading AI Model... Please wait."):
    model = load_model()

# Class Labels
class_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

# UI Layout
st.markdown("<h1 class='title-text'>🤟 Indian Sign Language (ISL) Recognition</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>Empowering communication through AI. Upload an image of a hand gesture to see the translation in real-time.</p>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("ℹ️ About the Project")
    st.info(
        "This deep learning application uses a Convolutional Neural Network (CNN) "
        "trained to recognize 24 static letters of the Indian Sign Language alphabet."
    )
    st.write("---")
    st.write("### 🛠️ How to use:")
    st.write("1. Take a clear picture of a hand gesture.")
    st.write("2. Upload the image using the drag-and-drop area.")
    st.write("3. Wait for the AI to analyze and predict the letter!")

# Main layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📷 Upload Image")
    # File uploader
    uploaded_file = st.file_uploader("Drag and drop your image here", type=["jpg", "jpeg", "png"])

with col2:
    st.markdown("### 🤖 AI Analysis")
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file).convert("RGB")
        
        # Preprocess the image
        img = image.resize((64, 64))
        img_array = np.array(img, dtype=np.float32)
        img_array = img_array / 255.0  # Rescale to match training preprocessing
        img_array = np.expand_dims(img_array, axis=0)
        
        # Make prediction
        with st.spinner("Analyzing gesture..."):
            predictions = model.predict(img_array)
            predicted_class_index = np.argmax(predictions, axis=1)[0]
            confidence = float(np.max(predictions))
            predicted_label = class_labels[predicted_class_index]
        
        # Show results in a nice box
        st.markdown(f"""
            <div class="prediction-box">
                <h2 style='color: #2563EB; font-size: 4rem; margin: 0;'>{predicted_label}</h2>
                <p style='color: #6B7280; font-size: 1.2rem; margin: 0;'>Predicted Letter</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("") # spacing
        st.write(f"**Confidence Level:** {confidence:.2%}")
        st.progress(confidence)
        
        if confidence > 0.90:
            st.balloons()
            st.success("High confidence prediction! ✨")
        elif confidence < 0.50:
            st.warning("Low confidence. Try uploading a clearer image with better lighting. 💡")

# Image preview at the bottom
if uploaded_file is not None:
    st.write("---")
    st.markdown("<h3 style='text-align:center;'>Image Preview</h3>", unsafe_allow_html=True)
    col3, col4, col5 = st.columns([1, 2, 1])
    with col4:
        st.image(image, caption='Analyzed Image', use_container_width=True)
else:
    st.info("👆 Please upload an image in the designated area to begin the analysis.")
