import streamlit as st
import html
from transformers import pipeline
# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="STARK AI",
    page_icon="⚡",
    layout="wide"
)

# --------------------------------------------------
# AVENGERS / STARK STYLE CSS
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Orbitron', sans-serif;
}

/* MAIN BACKGROUND */

.stApp {
    background:
        radial-gradient(circle at 50% 20%, #182848 0%, #080b14 45%, #020308 100%);
    color: white;
}

/* Remove default top padding */

.block-container {
    padding-top: 3rem;
    padding-left: 8%;
    padding-right: 8%;
}

/* MAIN TITLE */

.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: 900;
    letter-spacing: 8px;

    color: #ffffff;

    text-shadow:
        0 0 5px #00eaff,
        0 0 15px #00eaff,
        0 0 30px #008cff,
        0 0 60px #005eff;

    margin-bottom: 5px;
}

/* SUBTITLE */

.subtitle {
    text-align: center;
    color: #00eaff;
    font-size: 15px;
    letter-spacing: 5px;
    margin-bottom: 45px;

    text-shadow:
        0 0 8px #00eaff;
}

/* ARC REACTOR */

.reactor {
    width: 100px;
    height: 100px;

    margin: 0 auto 30px auto;

    border-radius: 50%;

    background: radial-gradient(
        circle,
        #ffffff 0%,
        #7df9ff 20%,
        #00d9ff 40%,
        #006eff 65%,
        #001b44 100%
    );

    box-shadow:
        0 0 15px #00eaff,
        0 0 30px #00eaff,
        0 0 60px #0077ff,
        0 0 100px #005eff;

    animation: reactorPulse 2s infinite alternate;
}

@keyframes reactorPulse {

    from {
        transform: scale(1);
        box-shadow:
            0 0 15px #00eaff,
            0 0 30px #00eaff,
            0 0 50px #0077ff;
    }

    to {
        transform: scale(1.08);
        box-shadow:
            0 0 25px #ffffff,
            0 0 50px #00eaff,
            0 0 90px #006eff;
    }
}

/* SECTION LABEL */

.section-label {
    color: #00eaff;
    font-size: 14px;
    letter-spacing: 3px;
    margin-bottom: 10px;
}

/* TEXT AREA */

textarea {

    background: rgba(5, 15, 30, 0.85) !important;

    color: #ffffff !important;

    border: 1px solid #00eaff !important;

    border-radius: 10px !important;

    box-shadow:
        0 0 10px rgba(0, 234, 255, 0.3),
        inset 0 0 20px rgba(0, 234, 255, 0.05) !important;

    font-family: 'Orbitron', sans-serif !important;

    font-size: 16px !important;
}

/* TEXT AREA FOCUS */

textarea:focus {

    border: 1px solid #ffffff !important;

    box-shadow:
        0 0 10px #00eaff,
        0 0 25px #0077ff,
        inset 0 0 15px rgba(0, 234, 255, 0.1) !important;
}

/* BUTTON */

.stButton > button {

    width: 100%;

    background: linear-gradient(
        90deg,
        #006eff,
        #00d9ff,
        #006eff
    );

    color: white;

    border: 1px solid #00eaff;

    border-radius: 8px;

    padding: 15px;

    font-family: 'Orbitron', sans-serif;

    font-size: 16px;

    font-weight: 700;

    letter-spacing: 3px;

    box-shadow:
        0 0 10px #00eaff,
        0 0 25px rgba(0, 119, 255, 0.6);

    transition: all 0.3s ease;
}

.stButton > button:hover {

    transform: scale(1.02);

    background: linear-gradient(
        90deg,
        #00d9ff,
        #ffffff,
        #00d9ff
    );

    color: #00142e;

    box-shadow:
        0 0 20px #00eaff,
        0 0 50px #0077ff;
}

/* OUTPUT HUD */

.output-box {

    margin-top: 35px;

    padding: 25px;

    background: rgba(3, 14, 30, 0.8);

    border: 1px solid #00eaff;

    border-radius: 12px;

    box-shadow:
        0 0 15px rgba(0, 234, 255, 0.4),
        inset 0 0 25px rgba(0, 234, 255, 0.05);

}

/* OUTPUT HEADER */

.output-title {

    color: #00eaff;

    font-size: 17px;

    letter-spacing: 3px;

    margin-bottom: 15px;

    text-shadow:
        0 0 10px #00eaff;
}

/* OUTPUT TEXT */

.output-text {

    color: #ffffff;

    font-family: monospace;

    font-size: 17px;

    line-height: 1.7;

}

/* STATUS */

.status {

    text-align: center;

    margin-top: 35px;

    color: #00ffcc;

    font-size: 12px;

    letter-spacing: 3px;

    text-shadow:
        0 0 10px #00ffcc;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="reactor"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">STARK AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">⚡ ADVANCED TEXT GENERATION SYSTEM ⚡</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
    )


generator = load_model()


# --------------------------------------------------
# INPUT
# --------------------------------------------------

st.markdown(
    '<div class="section-label">▸ INPUT COMMAND</div>',
    unsafe_allow_html=True
)

prompt = st.text_area(
    "",
    placeholder="Artificial Intelligence is...",
    height=150
)


# --------------------------------------------------
# GENERATE
# --------------------------------------------------
if st.button("⚡ INITIATE GENERATION"):

    if prompt:

        with st.spinner("⚡ STARK AI SYSTEM ONLINE..."):

            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ]

            result = generator(
                messages,
                max_new_tokens=200,
                do_sample=True,
                temperature=0.7,
                top_p=0.9
            )

        # Get the assistant's response
        generated_messages = result[0]["generated_text"]

        generated_text = generated_messages[-1]["content"]

        generated_text = html.escape(generated_text)

        output_html = f"""
<div class="output-box">
<div class="output-title">▸ GENERATED INTELLIGENCE</div>
<div class="output-text">{generated_text}</div>
</div>
"""

        st.markdown(
            output_html,
            unsafe_allow_html=True
        )

    else:

        st.warning("⚠️ INPUT REQUIRED — ENTER A COMMAND FIRST.")
# --------------------------------------------------
# STATUS
# --------------------------------------------------

st.markdown(
    '<div class="status">● SYSTEM STATUS : ONLINE</div>',
    unsafe_allow_html=True
)