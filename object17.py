import streamlit as st
from transformers import pipeline
from PIL import Image

# --------------------------------------------------
# Page settings
# --------------------------------------------------

st.set_page_config(
    page_title="AI Object Detector",
    page_icon="🤖",
    layout="centered"
)

st.title("🔍 AI Object Detection")
st.write("Upload an image and let AI identify the objects in it.")

# --------------------------------------------------
# Load Hugging Face model
# --------------------------------------------------

@st.cache_resource
def load_detector():
    return pipeline("object-detection")

detector = load_detector()

# --------------------------------------------------
# Upload image
# --------------------------------------------------

image = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------------------------
# Detection
# --------------------------------------------------

if image:

    img = Image.open(image).convert("RGB")

    st.image(
        img,
        caption="Uploaded Image",
        width=500
    )

    if st.button("🔍 Detect Objects"):

        with st.spinner("Detecting objects..."):
            results = detector(img)

        st.subheader("🎯 Detected Objects")

        if results:

            for result in results:
                label = result["label"]
                score = result["score"]

                st.write(
                    f"**{label}** — "
                    f"{score * 100:.2f}% confidence"
                )

        else:
            st.warning("No objects detected.")