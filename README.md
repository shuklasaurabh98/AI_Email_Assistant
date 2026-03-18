# AI Email Assistant

An intelligent web-based application that generates professional emails using AI.
Built using **Flask** and **Google Gemini API**, this tool helps users quickly create well-structured emails with different tones and purposes.

---

## Features

* AI-powered email generation using **Gemini 2.5 Flash**
* Supports multiple tones (Formal, Friendly, Professional, Apologetic)
* Custom inputs:

  * Subject
  * Purpose
  * Recipient
  * Key points
  * Sender name
* Automatically generates structured email (greeting + body + closing)
* Copy-to-clipboard functionality
* Direct "Send via Gmail" integration
* Modern responsive UI (glassmorphism design)

---

## Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **AI Model:** Google Gemini API (`gemini-2.5-flash`)
* **Environment Management:** python-dotenv

---

## Project Structure

```
AI_Email_Assistant/
│── app.py
│── email_generator.py
│── templates/
│     └── index.html
│── static/
│── .env
│── .gitignore
│── requirements.txt
```

---

## Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/AI_Email_Assistant.git
cd AI_Email_Assistant
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the application

```
python app.py
```

---

### 6️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## How It Works

1. User fills the form (subject, tone, key points, etc.)
2. Flask backend sends prompt to Gemini API
3. AI generates a structured email
4. Output is displayed on UI
5. User can copy or send via Gmail

---

## Security Note

use your own API Key

--

## Future Improvements

* Email templates (job application, leave request, etc.)
* Multi-language support
* Save email history
* User authentication system
* Direct email sending via SMTP

---
## 📸 Screenshots

### 🏠 Home Page
<img width="1842" height="968" alt="Screenshot from 2026-03-18 12-46-35" src="https://github.com/user-attachments/assets/20d1dd26-8877-4d78-846b-b3f6dfa2038f" />


