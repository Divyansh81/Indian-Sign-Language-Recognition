# 🤟 Indian Sign Language (ISL) Recognition

Welcome to the **Indian Sign Language (ISL) Recognition** project! This repository contains a deep learning solution designed to recognize and translate static Indian Sign Language alphabet gestures into text. 

Our goal is to bridge the communication gap for the hearing-impaired community by leveraging the power of Artificial Intelligence.

---

## 🌟 What Does This Project Do?

This project uses a **Convolutional Neural Network (CNN)** (a type of AI designed for images) to look at a picture of a hand gesture and tell you which letter of the Indian Sign Language alphabet it represents. 

It can currently recognize **24 unique sign gestures**.

### Key Highlights:
- **Smart AI Model:** Built with TensorFlow and Keras.
- **Robust Training:** The AI is trained on images that have been rotated, zoomed, and flipped to make it better at recognizing gestures from different angles (Data Augmentation).
- **Interactive Web App:** We've built a user-friendly Streamlit web application where anyone can upload a picture of a hand gesture and get an instant translation.
- **Automated Setup:** The code handles downloading and preparing the dataset for you automatically.

---

## 📁 What's Inside?

- `app.py`: The code for the interactive Streamlit web application.
- `project.ipynb`: A Jupyter Notebook containing the full code for downloading the data, training the AI model, and evaluating its performance.
- `isl_recognition_model.h5`: The trained AI model (ready to use!).
- `requirements.txt`: A list of all the Python tools needed to run this project.
- Sample images (`.jpg`): A few example images you can use to test the app.

---

## 📸 App Interface

Here is what our web app looks like:

<p align="center">
  <img src="Screenshot_1%20(1).png" alt="App Screenshot 1" width="800"/>
  <br><br>
  <img src="Screenshot_2.png" alt="App Screenshot 2" width="800"/>
</p>

---

## 🚀 How to Run the App on Your Computer

Want to try it yourself? Follow these simple steps:

### 1. Download the Project
First, get a copy of this project on your computer:
```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 2. Install the Required Tools
Make sure you have Python installed, then run this command to install the necessary libraries:
```bash
pip install -r requirements.txt
```

### 3. Launch the Web App
Start the interactive application by running:
```bash
streamlit run app.py
```
A new tab will open in your web browser where you can upload images and see the AI in action!

### 4. (Optional) Explore the Code
If you want to see how the AI was trained, you can open the Jupyter Notebook:
```bash
jupyter notebook project.ipynb
```

---

## 📝 A Note on Data
When you run the `project.ipynb` notebook, it will automatically download the required dataset and extract it into a folder named `ISL_Data_Extracted`. Don't worry—this folder is ignored by Git, so it won't clutter your repository!
