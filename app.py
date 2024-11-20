import streamlit as st
from PIL import Image
import numpy as np
import cv2
from transformations import translate_image, scale_image, rotate_image, shear_image

# Title and Description
st.title("Image Transformation - Affine Transformations")
st.write("Upload an image and apply various affine transformations.")

# Image Upload
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "png"])

if uploaded_image:
    # Convert the uploaded file to a NumPy array
    image = Image.open(uploaded_image)
    st.image(image, caption="Original Image", use_column_width=True)
    image_np = np.array(image)

    # Transformation Options
    st.subheader("Choose a Transformation")
    transformation = st.selectbox("Transformation Type", ["Translation", "Scaling", "Rotation", "Shearing"])

    if transformation == "Translation":
        tx = st.slider("Translate X", -200, 200, 0)
        ty = st.slider("Translate Y", -200, 200, 0)
        transformed_image = translate_image(image_np, tx, ty)

    elif transformation == "Scaling":
        sx = st.slider("Scale X", 0.1, 3.0, 1.0)
        sy = st.slider("Scale Y", 0.1, 3.0, 1.0)
        transformed_image = scale_image(image_np, sx, sy)

    elif transformation == "Rotation":
        angle = st.slider("Rotation Angle", -180, 180, 0)
        transformed_image = rotate_image(image_np, angle)

    elif transformation == "Shearing":
        shear_x = st.slider("Shear X", -1.0, 1.0, 0.0)
        shear_y = st.slider("Shear Y", -1.0, 1.0, 0.0)
        transformed_image = shear_image(image_np, shear_x, shear_y)

    # Display Transformed Image
    st.subheader("Transformed Image")
    st.image(transformed_image, caption="Transformed Image", use_column_width=True)

    # Download Option
    result = Image.fromarray(transformed_image)
    st.download_button("Download Transformed Image", data=result.tobytes(), file_name="transformed_image.png")

