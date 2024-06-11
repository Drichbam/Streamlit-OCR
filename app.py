import streamlit as st
import numpy as np
from PIL import Image
import easyocr as ocr

st.title("OCR Text Extraction from Image")
st.markdown("MVP using **Streamlit** and **EasyOCR** (en, es, fr)")
st.markdown("")


# load OCR models
@st.cache_resource()
def load_models():
    reader = ocr.Reader(["en", "es", "fr"], model_storage_directory=".")
    return reader


reader = load_models()


def image_to_text(img_file_buffer=None):
    if img_file_buffer is not None:
        # Read image from buffer
        image = Image.open(img_file_buffer)
        st.image(image, caption="Captured Image", use_column_width=True)

        with st.spinner("OCR in progress..."):
            # Convert image to numpy array
            img_array = np.array(image)

            # OCR easyOCR
            results = reader.readtext(img_array)
            extracted_text = "\n".join([text for (_, text, _) in results])

    return extracted_text


img_file_buffer = None
image_input = st.radio(
    "Choose how to input text:",
    ["Camera", "Image"],
    captions=[
        "use your webcam to scan some text",
        "upload an image file 'png', 'jpg' or 'jpeg'",
    ],
    index=None,
)

if image_input == "Camera":
    st.write("You selected camera.")
    img_file_buffer = st.camera_input("Take a picture")
elif image_input == "Image":
    st.write("You selected image.")
    img_file_buffer = st.file_uploader(
        label="Upload your image here", type=["png", "jpg", "jpeg"]
    )
else:
    st.write("Select an option.")

if img_file_buffer is not None:
    extracted_text = image_to_text(img_file_buffer)
    # Display the extracted text
    st.subheader("Extracted Text")
    st.text(extracted_text)
    st.balloons()
