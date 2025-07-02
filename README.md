# 🤖 AI Health Assistant Chatbot

This project is an AI-powered health assistant chatbot built using **Gradio** and **Hugging Face Transformers**. It uses Microsoft's `phi-1_5` language model to answer general health-related questions.

---

## 🏗️ Folder Structure

```
health-chatbot/
├── gradio_app.py       # Main Gradio web interface script
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## 🌐 Model Access via Hugging Face

Instead of using a local version, the model is fetched directly from Hugging Face’s public repository:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1_5")
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-1_5", trust_remote_code=True)
```

✅ **Note**: Ensure your machine has internet access when running this the first time.

If you're running in a restricted environment or want faster access later, Hugging Face will cache the model locally after the first use.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/health-chatbot.git
cd health-chatbot
```

### 2. Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Unix/Mac:
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Gradio App

```bash
python gradio_app.py
```

Then open the local Gradio interface in your browser (usually http://localhost:7860/).

---

## ✏️ Sample Usage

- **Input**: What are the symptoms of diabetes?
- **Output**: [AI-generated response from the `phi-1_5` model]

---

## ✅ Requirements

- Python 3.7+
- gradio
- transformers
- torch

You can install all dependencies using:

```bash
pip install gradio transformers torch
```

---

## 📬 Contact

For questions or contributions, feel free to open an issue or fork this project.

---

## 🔐 License

This project is open-source under the MIT License.
