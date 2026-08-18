# 🔍 AI Object Detection

A simple **AI-powered object detection web application** built using **Python, Streamlit, Hugging Face Transformers, and PIL**.

The application allows users to upload an image and uses a pre-trained Hugging Face object detection model to identify objects present in the image and display their confidence scores.

---

## 🚀 Features

* 🤖 AI-powered object detection
* 📸 Upload JPG, JPEG, and PNG images
* 🔍 Automatically identify objects in images
* 📊 Display confidence percentage for each detected object
* ⚡ Fast and simple Streamlit interface
* 🧠 Uses a pre-trained Hugging Face model
* 💾 Model is cached to avoid unnecessary reloading

---

## 🛠️ Technologies Used

| Technology                    | Purpose                      |
| ----------------------------- | ---------------------------- |
| **Python**                    | Core programming language    |
| **Streamlit**                 | Web application interface    |
| **Hugging Face Transformers** | Object detection pipeline    |
| **Pillow (PIL)**              | Image loading and processing |

---

## 🧠 AI Model

The project uses the Hugging Face Transformers object detection pipeline:

```python
pipeline("object-detection")
```

Since no specific model is provided, Transformers loads the default model associated with the object-detection pipeline.

The model processes the uploaded image and returns detected objects along with their confidence scores and bounding-box information.

---

## 📂 Project Structure

```text
AI-Object-Detection/
│
├── object_detection.py
├── README.md
└── requirements.txt
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the project directory:

```bash
cd AI-Object-Detection
```

---

### 2. Create a Virtual Environment

For Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install streamlit transformers torch pillow
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the following command:

```bash
streamlit run object_detection.py
```

The application will open in your browser.

The default Streamlit address is usually:

```text
http://localhost:8501
```

---

## 🖼️ How to Use

### Step 1 — Upload an Image

Click:

**Upload an image**

and select a `.jpg`, `.jpeg`, or `.png` image.

### Step 2 — Preview the Image

The uploaded image will be displayed in the application.

### Step 3 — Detect Objects

Click:

**🔍 Detect Objects**

The AI model will analyze the image.

### Step 4 — View Results

The application displays each detected object and its confidence score.

Example:

```text
person — 98.42% confidence

dog — 95.17% confidence

car — 91.63% confidence
```

---

## 🔄 Application Workflow

```text
        ┌─────────────────┐
        │   Upload Image  │
        └────────┬────────┘
                 ↓
        ┌─────────────────┐
        │  Convert to RGB │
        └────────┬────────┘
                 ↓
        ┌─────────────────┐
        │ Hugging Face AI │
        │ Object Detector │
        └────────┬────────┘
                 ↓
        ┌─────────────────┐
        │ Detect Objects  │
        └────────┬────────┘
                 ↓
        ┌─────────────────┐
        │ Confidence      │
        │ Scores          │
        └─────────────────┘
```

---

## 📊 Detection Results

Each detection returned by the model contains information such as:

| Information      | Description                         |
| ---------------- | ----------------------------------- |
| **Label**        | Name of the detected object         |
| **Score**        | Model confidence                    |
| **Bounding Box** | Location of the object in the image |

The current application displays the **object label** and **confidence percentage**.

---

## ⚡ Model Caching

The application uses Streamlit's resource caching:

```python
@st.cache_resource
def load_detector():
    return pipeline("object-detection")
```

This prevents the model from being loaded repeatedly every time Streamlit reruns the application.

This makes subsequent interactions faster.

---

## ⚠️ Notes

### First Run

The first execution may take longer because Hugging Face may need to download the required model.

The model is then cached locally.

### Hardware

Object detection can run on a CPU, although inference may be slower on systems without a GPU.

---

## 🔮 Future Improvements

Possible upgrades for this project include:

* 📦 Draw bounding boxes around detected objects
* 🎯 Display confidence directly on the image
* 📊 Add a detection statistics dashboard
* 📸 Support webcam input
* 🎥 Add real-time video object detection
* 🔢 Allow users to set a confidence threshold
* 🧠 Allow users to select different object detection models
* 💾 Download detection results
* 🌐 Deploy the application online

---

## 📚 Learning Concepts Demonstrated

This project demonstrates:

* Artificial Intelligence
* Computer Vision
* Object Detection
* Pre-trained AI Models
* Hugging Face Transformers
* Model Inference
* Image Processing
* Streamlit
* Python
* Confidence Scores
* AI Application Development

---

## 👩‍💻 Author

**Asiya**

B.Sc. Computer Science with Artificial Intelligence

---

## ⭐ Project

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

**AI OBJECT DETECTION — READY TO SEE WHAT'S IN THE IMAGE! 🤖**
