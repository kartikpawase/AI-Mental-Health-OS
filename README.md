# 🧬 AI Mental Health Operating System
### *Intelligent Mental Health Prediction & Monitoring Platform — 2050 Vision*

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red?style=for-the-badge&logo=pytorch)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)
![Gemini AI](https://img.shields.io/badge/Google-Gemini%20AI-4285F4?style=for-the-badge&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Built by [Kartik Pawase](https://github.com/kartikpawase)**

</div>

---

## 🎯 What is This?

The **AI Mental Health Operating System** is a production-level, multi-modal AI healthcare platform designed with a **2050 vision**. It moves beyond simple mental health screening to provide a complete, continuously-monitoring, intelligent digital health assistant.

> *"This isn't just a prediction app — it's a full digital mental health ecosystem."*

---

## ✨ Features

### 🤖 Core AI Capabilities
| Feature | Description |
|---------|-------------|
| **Deep Neural Network** | PyTorch ResNet-style DNN trained on biometric data for depression risk prediction (81%+ accuracy) |
| **Gemini AI Therapist** | Real Google Gemini LLM-powered chatbot providing evidence-based CBT therapy |
| **Explainable AI (SHAP)** | SHAP value waterfall charts explaining *why* every prediction was made |
| **Multi-Modal Analysis** | Live microphone voice sentiment + facial micro-expression AI via webcam |

### 📊 Monitoring & Analytics
| Feature | Description |
|---------|-------------|
| **Real-Time Risk Dashboard** | Live biometric sliders feeding Plotly gauge charts and risk scoring |
| **Digital Twin** | 14-day AI forecasting of your mental health trajectory |
| **Early Warning System** | Automatic crisis alerts when risk exceeds 85% threshold |
| **30-Day Trend Tracker** | Historical mood and risk graph visualisation |

### 🔬 Advanced 2050 Features
| Feature | Description |
|---------|-------------|
| **🧠 EEG Brainwave Monitor** | Live Alpha/Beta/Theta/Delta wave simulation and mental state classification |
| **😴 Sleep Intelligence AI** | Predicts tonight's sleep quality + 30-day sleep debt tracker |
| **🧬 Genomic Risk Mapper** | DNA-based radar chart of inherited psychiatric condition risks |
| **🌍 Community Health Map** | Anonymised city-level depression heatmap across India |
| **🔐 Privacy Control Centre** | HIPAA-style consent management, anonymous mode, E2E encryption toggles |
| **⚖️ Bias & Fairness Monitor** | Demographic fairness radar ensuring model equality across genders and ages |

---

## 🛠️ Tech Stack

```
Frontend    →  Streamlit (Custom Glassmorphism CSS + Plotly)
Backend     →  FastAPI (Async REST API + SQLAlchemy ORM)
AI/ML       →  PyTorch (Deep Neural Network) + Scikit-learn
LLM         →  Google Gemini 1.5 Flash API
Database    →  SQLite (→ PostgreSQL ready)
Deployment  →  Docker + Docker Compose (AWS EC2 ready)
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/kartikpawase/AI-Mental-Health-OS.git
cd AI-Mental-Health-OS
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Gemini AI (FREE API Key)
Create `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your-gemini-api-key-here"
```
Get a free key at: https://aistudio.google.com/app/apikey

### 4. Train the AI Model
```bash
python data/generate_synthetic.py
python ai_models/train.py
```

### 5. Launch Backend API
```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

### 6. Launch Frontend Dashboard
```bash
python -m streamlit run frontend/app.py
```

🌐 Open `http://localhost:8501` in your browser.

---

## 📁 Project Structure

```
AI Mental Health OS/
├── 📂 frontend/
│   ├── app.py                  # 🏠 Landing page
│   └── pages/
│       ├── 1_Dashboard.py      # 📊 Real-time risk dashboard
│       ├── 2_Therapist.py      # 🤖 Gemini AI chatbot
│       ├── 3_MultiModal.py     # 🎤 Voice + Face AI
│       ├── 4_DigitalTwin.py    # 🔮 Future risk forecasting
│       ├── 5_Insights.py       # 🧠 XAI + Fairness
│       ├── 6_Privacy.py        # 🔐 Privacy controls
│       ├── 7_BrainwaveEEG.py   # ⚡ EEG monitor
│       ├── 8_SleepAI.py        # 😴 Sleep intelligence
│       ├── 9_Genomics.py       # 🧬 DNA risk mapper
│       └── 10_CommunityMap.py  # 🌍 Community health map
├── 📂 backend/
│   ├── main.py                 # FastAPI routes
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic schemas
│   ├── database.py             # DB connection
│   └── security.py             # Auth & encryption
├── 📂 ai_models/
│   ├── neural_net.py           # PyTorch DNN architecture
│   ├── train.py                # Training pipeline
│   ├── nlp_engine.py           # Sentiment analysis
│   └── multimodal.py           # Multi-modal processors
├── 📂 data/
│   ├── generate_synthetic.py   # Synthetic data generator
│   └── preprocess.py           # ML preprocessing pipeline
├── 📂 deployment/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── start.sh
├── requirements.txt
└── README.md
```

---

## 🐳 Docker Deployment

```bash
docker-compose -f deployment/docker-compose.yml up -d --build
```

This automatically starts:
- **FastAPI** on `http://localhost:8000`
- **Streamlit** on `http://localhost:8501`

---

## 🤖 AI Model Performance

| Metric | Score |
|--------|-------|
| **Accuracy** | 81.4% |
| **F1 Score** | 82.1% |
| **Architecture** | Residual DNN (PyTorch) |
| **Training Data** | 5,000 synthetic biometric samples |
| **Input Features** | 8 biometric + NLP sentiment |

---

## 🔐 Privacy & Ethics

- ✅ All user data is processed **locally** — nothing sent to external servers
- ✅ Anonymous mode available — zero PII stored
- ✅ SHAP explainability — no black-box decisions in healthcare
- ✅ Fairness monitoring across demographics (gender, age groups)
- ✅ Crisis detection with immediate helpline routing

**India Crisis Helpline:** iCall — `9152987821` | Vandrevala Foundation — `1860-2662-345`

---

## 👨‍💻 Author

**Kartik Pawase**
- GitHub: [@kartikpawase](https://github.com/kartikpawase)

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">
<i>Built with ❤️ for the future of mental healthcare — 2050 Vision 🚀</i>
</div>
