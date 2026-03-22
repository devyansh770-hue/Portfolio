# 🧑‍💻 Devyansh Verma — Portfolio

A production-grade Django portfolio with an AI-powered Gemini chat widget, project showcases, blog, contact form, and dark/light mode.

---

## ✨ Features

- **AI Chat Widget** — Gemini-powered floating chatbot trained on your CV context
- **Projects Showcase** — Case study-style project pages with problem/solution/impact
- **Blog** — Admin-editable posts via Django Admin
- **Contact Form** — Saves messages to DB + sends email via Gmail SMTP
- **Dark / Light Mode** — CSS variable theming, persisted in localStorage
- **Scroll Animations** — AOS.js powered entrance animations
- **Typewriter Hero** — Animated role cycling on homepage
- **Responsive** — Mobile-first, hamburger nav

---

## 🗂️ Project Structure

```
devyansh_portfolio/
├── portfolio_project/      # Django settings, urls, wsgi
├── core/                   # Home, About pages
├── projects/               # Project showcase (hardcoded)
├── blog/                   # Blog (DB-backed, admin editable)
├── contact/                # Contact form
├── ai_chat/                # Gemini API endpoint
├── templates/              # All HTML templates
│   ├── base.html           # Master layout (navbar, chat widget, footer)
│   ├── core/
│   ├── projects/
│   ├── blog/
│   └── contact/
├── static/                 # CSS, JS, images
├── manage.py
├── requirements.txt
├── .env.example
└── setup.sh
```

---

## ⚡ Quick Start

### 1. Clone & navigate
```bash
git clone <your-repo>
cd devyansh_portfolio
```

### 2. Run setup script
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Configure `.env`
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
GEMINI_API_KEY=your-gemini-api-key
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

> **Getting a Gemini API key:** Go to [aistudio.google.com](https://aistudio.google.com) → Get API Key (free tier available)

> **Gmail App Password:** Google Account → Security → 2-Step Verification → App Passwords

### 4. Run the server
```bash
source venv/bin/activate
python manage.py runserver
```

Open **http://127.0.0.1:8000** 🎉

---

## 🔑 Django Admin

Visit **http://127.0.0.1:8000/admin/** to:
- Add / edit **Blog Posts**
- View **Contact Messages**

---

## 📝 Adding Blog Posts

1. Go to `/admin/`
2. Click **Blog posts → Add**
3. Fill in title, excerpt, content (supports HTML via `linebreaks` filter), and comma-separated tags
4. Check **Published** and save

---

## 🤖 AI Chat Configuration

The chat widget is pre-prompted with your full CV data in `ai_chat/views.py`.

To customise what the AI knows, edit the `DEVYANSH_CONTEXT` string in `ai_chat/views.py`.

If `GEMINI_API_KEY` is not set, the widget gracefully falls back to a contact redirect message.

---

## 🚀 Deployment (Render / Railway)

1. Set all `.env` variables as environment variables on your platform
2. Set `DEBUG=False`
3. Run `python manage.py collectstatic`
4. Point your platform's start command to:
   ```
   gunicorn portfolio_project.wsgi:application
   ```

---

## 🛠️ Tech Stack

| Layer | Tech |
|---|---|
| Backend | Django 4.2 |
| AI | Google Gemini 1.5 Flash |
| Database | SQLite (swap to PostgreSQL for production) |
| Styling | Custom CSS + CSS Variables |
| Animations | AOS.js |
| Fonts | Syne + DM Mono + DM Sans |
| Email | Django send_mail + Gmail SMTP |

---

Built with 💚 by **Devyansh Verma**
