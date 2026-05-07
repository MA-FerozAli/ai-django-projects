

I have updated your README to mark the **Joke Generator** and **Grammar Fixer** as complete and added the **SEO Meta Data Generator** to the "Upcoming" slot with a brief spotlight.

---

# 🤖 AI Django Projects

A collection of AI-powered web apps built with Django + Gemini API.

---

## 🟢 Level 1 — The Basics

| # | Project | Status |
|---|---------|--------|
| 1 | AI Text Summarizer | ✅ Done |
| 2 | Dictionary+ | ✅ Done |
| 3 | AI Joke & Quote Generator | ✅ Done |
| 4 | Grammar & Tone Fixer | ✅ Done |
| 5 | SEO Meta Data Generator | ✅ Done |

---
## Level 2 - State & Memory
| # | Project | Status |
|---|---------|--------|
| 1 | AI ChatBot |  ⏳ Upcomming |
| 2 |Blog Architect | ⏳ Upcomming |
## 📖 Project Spotlights

### **Dictionary+**
Uses strict JSON prompting to return structured linguistic data including phonetics, etymology, and synonyms.

### **Joke & Grammar Tools**
* **Joke Generator**: Leverages AI to generate context-specific humor based on user-provided themes.
* **Grammar & Tone Fixer**: Analyzes text for errors and allows users to shift the "vibe" (Professional, Casual, or Witty).

### **SEO Meta Data Generator (Next Up!)**
This tool will take a URL or a block of content and automatically generate optimized **Meta Titles**, **Descriptions**, and **Keywords** to improve search engine rankings.

### AI TEXT SUMMARIZER
takes a long input of text return consice summary

# Started Implementing the AI Chatbot

## started implementing of Blog Architect 
---

## ⚙️ Tech Stack
- **Backend**: Python 3.12+ & Django 5.0+
- **AI Engine**: Google Gemini API (`gemini-2.5-flash`)
- **Environment**: `python-dotenv` for API key security

---

## 🚀 How to Run Locally

1. **Clone & Setup:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-django-projects.git
   cd ai-django-projects
   python -m venv venv
   source venv/bin/activate  # venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. **Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_key_here
   ```

3. **Database & Server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

### 💡 Pro-Tip
As you saw with the **Dictionary+** app, you might hit a `429 RESOURCE_EXHAUSTED` error. This is a standard rate limit for the Gemini Free Tier. Simply wait about **30–60 seconds** before making another request.

---
