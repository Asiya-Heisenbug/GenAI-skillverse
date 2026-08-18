# ⚡ STARK AI — Advanced Text Generation System

A futuristic **AI-powered text generation web application** built with **Python, Streamlit, and Hugging Face Transformers**.

STARK AI features a sleek **Iron Man / Arc Reactor-inspired interface** and uses the **DeepSeek-R1-Distill-Qwen-1.5B** language model to generate intelligent text responses from user prompts.

---

## 🚀 Features

* ⚡ Futuristic STARK / Arc Reactor-inspired UI
* 🤖 AI-powered text generation
* 🧠 DeepSeek-R1-Distill-Qwen-1.5B model
* 🎛️ Adjustable text-generation parameters
* 🌌 Custom animated interface
* 💬 Simple prompt-based interaction
* 🔥 Neon blue HUD-style design
* 📱 Streamlit-based web interface
* 🛡️ HTML escaping for generated output

---

## 🛠️ Technologies Used

| Technology                        | Purpose                               |
| --------------------------------- | ------------------------------------- |
| **Python**                        | Core programming language             |
| **Streamlit**                     | Web application framework             |
| **Hugging Face Transformers**     | AI model and text-generation pipeline |
| **DeepSeek R1 Distill Qwen 1.5B** | Text generation model                 |
| **HTML/CSS**                      | Custom UI and styling                 |

---

## 🧠 AI Model

STARK AI uses:

**`deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B`**

This is a distilled language model based on the Qwen architecture and designed to provide useful text-generation capabilities while being considerably smaller than large-scale models.

The application loads the model through the Hugging Face Transformers `pipeline()` API:

```python
pipeline(
    "text-generation",
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
)
```

---

## 📂 Project Structure

```text
STARK-AI/
│
├── app.py
├── README.md
└── requirements.txt
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Move into the project directory:

```bash
cd STARK-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit transformers torch
```

Or, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## 💬 How to Use

1. Launch STARK AI.
2. Enter a prompt in the **INPUT COMMAND** text box.
3. Click **⚡ INITIATE GENERATION**.
4. The AI model processes the prompt.
5. The generated response appears under **GENERATED INTELLIGENCE**.

### Example Prompt

```text
Artificial Intelligence is
```

STARK AI will continue the text using the loaded language model.

---

## ⚙️ Generation Parameters

The application currently uses:

| Parameter        |  Value | Purpose                        |
| ---------------- | -----: | ------------------------------ |
| `max_new_tokens` |  `200` | Maximum number of new tokens   |
| `temperature`    |  `0.7` | Controls randomness            |
| `top_p`          |  `0.9` | Controls token sampling        |
| `do_sample`      | `True` | Enables probabilistic sampling |

These parameters can be modified inside `app.py` to change the model's generation behavior.

---

## 🎨 Interface

The interface is designed around a futuristic **AI command-center / Arc Reactor aesthetic**.

### UI Elements

* ⚡ Animated Arc Reactor
* 🔵 Neon blue glow effects
* 🌌 Dark futuristic background
* 🤖 STARK AI title
* 💻 HUD-style output panel
* 🎛️ Futuristic input interface
* 🟢 System status indicator

---

## 📋 Requirements

Recommended environment:

```text
Python 3.10+
Streamlit
PyTorch
Transformers
```

The model may require several GB of storage and sufficient RAM because the language model is downloaded locally the first time the application runs.

---

## ⚠️ Notes

### First Run

The first execution may take longer because Hugging Face needs to download the model.

After downloading, the model is cached locally.

### Hardware

Performance depends on your hardware.

A GPU can significantly improve generation speed, while CPU-only execution may be slower.

---

## 🔮 Future Improvements

Possible future upgrades include:

* 🎤 Voice input
* 🔊 Text-to-speech responses
* 💬 Conversation history
* 🧠 Persistent AI memory
* 🌐 API integration
* 📄 Chat export
* 🎨 Multiple AI themes
* ⚙️ User-controlled generation parameters
* 🤖 AI assistant mode
* 📊 Token and generation statistics
* 🚀 GPU acceleration

---

## 📚 Learning Concepts Demonstrated

This project demonstrates practical concepts in:

* Large Language Models (LLMs)
* Generative AI
* Prompt engineering
* Text generation
* Hugging Face Transformers
* Model inference
* Temperature and sampling
* Streamlit application development
* Custom HTML/CSS in Streamlit
* AI model deployment

---

## 👩‍💻 Author

**Asiya**

B.Sc. Computer Science with Artificial Intelligence

---

## ⭐ Project

If you found this project interesting, consider giving the repository a ⭐ on GitHub!

> **"Sometimes you gotta run before you can walk."** ⚡

**STARK AI — SYSTEM STATUS: ONLINE**
