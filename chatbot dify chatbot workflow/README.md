**README.md**

```markdown
# Dual-Persona Interactive AI Chatbot (STEM Tutor & Rocky Persona)

An intelligent, interactive AI Chatflow built on [Dify AI](https://udify.app/chat/Pc7uyBGuvPn7PcfO). This project features a **Dual-Node LLM Architecture** that routes user queries between an engaging sci-fi character companion and a structured academic assistant.

🔗 **Live Web App Demo:** [Try the Chatbot on Dify](https://udify.app/chat/Pc7uyBGuvPn7PcfO)

---

## 🌟 Key Features

* **Dual-Persona Architecture:** Automatically detects user intent to switch between character dialogue and academic assistance.
* **Rocky Persona (Eridian Science Expert):** Emulates Rocky from Andy Weir’s *Project Hail Mary* using authentic translated speech patterns (third-person grammar, stripped articles, function tags like `Question:` and `Statement:`).
* **STEM Tutor Node:** Answers academic, homework, and syllabus queries in standard English with bullet points and step-by-step logic.
* **Intent Classification:** Uses a Question Classifier router node to direct casual/sci-fi questions to Rocky and study queries to the STEM Tutor.

---

## 🏗️ Architecture & Workflow

```text
               ┌──► [Class 1: Rocky/Sci-Fi] ──► [LLM: Rocky Node] ───────┐
[START Node] ──┼                                                        ├──► [ANSWER Node]
               └──► [Class 2: Academic/STEM] ─► [LLM: STEM Tutor Node] ──┘

```

### Component Breakdown

1. **Start Node:** Accepts incoming user messages and session variables.
2. **Question Classifier Node:** Routes execution based on classification rules:
* **Class 1 (Rocky):** Casual chat, space topics, engineering, or direct interaction with Rocky.
* **Class 2 (STEM Tutor):** Homework, concept explanations, math proofs, code debugging, or science queries.


3. **LLM Node (Rocky Persona):** Configured with custom few-shot example pairs and strict Eridian speech guidelines.
4. **LLM 2 Node (STEM Tutor):** Configured for clear, structured, professional explanations in standard English.
5. **Answer Node:** Dynamically renders the generated response from the active LLM branch to the user interface.

---

## 🚀 How to Run & Test

1. Access the web interface via the [Dify Web App](https://udify.app/chat/Pc7uyBGuvPn7PcfO).
2. **Test Rocky Persona:**
* Try: *"Who are you?"* or *"How does xenonite work?"*
* Expected: Rocky replies in third-person Eridian dialect (e.g., *"Statement: Xenonite very strong material!"*).


3. **Test STEM Tutor Persona:**
* Try: *"Explain photosynthesis step-by-step"* or *"Help me solve a calculus problem."*
* Expected: The chatbot provides a clear, structured, standard English explanation with bullet points.



---

## 🛠️ Built With

* **Platform:** [Dify.ai](https://dify.ai) (Chatflow Workflow Engine)
* **Models:** OpenAI GPT-5 / GPT-5.4-mini

```

```
