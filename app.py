import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pytesseract

# Configure the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

st.title("OCR Text Extraction from Image")
st.markdown("## MVP using tesseract OCR and streamlit")
st.markdown("")

# Camera input
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # Read image from buffer
    image = Image.open(img_file_buffer)
    st.image(image, caption='Captured Image', use_column_width=True)

    # Convert image to numpy array
    img_array = np.array(image)

    # Convert color space from BGR to RGB
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

    # Perform OCR
    text = pytesseract.image_to_string(img_array)

    # Display the extracted text
    st.subheader("Extracted Text")
    st.text(text)