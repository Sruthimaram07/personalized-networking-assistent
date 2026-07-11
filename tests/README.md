# 🤝 Personalized Networking Assistant

## 📌 Project Overview

The Personalized Networking Assistant is an AI-powered web application that helps users generate personalized conversation starters for networking events. It extracts important keywords from event descriptions, generates AI-based conversation starters, verifies facts using Wikipedia, stores conversations in a database, and allows users to provide feedback.

---

## 🚀 Features

- AI-based Conversation Starter Generation
- DistilBERT Keyword Extraction
- GPT-2 Text Generation
- Wikipedia Fact Checking
- SQLite Database Storage
- Conversation History
- User Feedback System
- Streamlit Frontend
- FastAPI Backend
- REST API Support
- Unit Testing using Pytest

---

## 🛠 Technologies Used

- Python
- FastAPI
- Streamlit
- Transformers (DistilBERT & GPT-2)
- SQLite
- SQLAlchemy
- Wikipedia API
- Pytest

---

## 📂 Project Structure

```text
PersonalizedNetworkingAssistant/
│── backend/
│── models/
│── tests/
│── venv/
│── main.py
│── frontend.py
│── networking.db
│── README.md
```

---

## ▶️ Run the Backend

```bash
uvicorn main:app --reload
```

---

## ▶️ Run the Frontend

```bash
streamlit run frontend.py
```

---

## 🧪 Run Unit Tests

```bash
pytest
```

---

## 📖 API Endpoints

- GET /
- POST /generate
- GET /fact-check/{topic}
- GET /history
- POST /feedback

---

## 👩‍💻 Developed By

**Sruthi Maram**