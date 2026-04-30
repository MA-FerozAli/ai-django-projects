# 🤖 AI Django Projects

A collection of AI-powered web apps built with Django + Gemini API.

---

## 🟢 Level 1 — The Basics

| # | Project | Status |
|---|---------|--------|
| 1 | AI Text Summarizer | ✅ Done |
| 2 | Joke & Quote Generator | 🔄 In Progress |
| 3 | Grammar & Tone Fixer | ⏳ Upcoming |

---

## ⚙️ Tech Stack
- Python 3.12+
- Django 5.0+
- Google Gemini API
- python-dotenv

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/ai-django-projects.git
cd ai-django-projects
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:
```
GEMINI_API_KEY=your_key_here
```

```bash
python manage.py migrate
python manage.py runserver
```