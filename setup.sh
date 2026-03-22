#!/bin/bash
# ─────────────────────────────────────────────
#  Devyansh Portfolio — Quick Setup Script
# ─────────────────────────────────────────────

echo ""
echo "🚀 Setting up Devyansh Portfolio..."
echo ""

# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# 3. Copy .env example if .env doesn't exist
if [ ! -f .env ]; then
  cp .env.example .env
  echo "⚠️  .env file created from .env.example"
  echo "    → Add your GEMINI_API_KEY and EMAIL credentials before running."
fi

# 4. Run migrations
echo "🗄️  Running migrations..."
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser (optional)
echo ""
echo "🔐 Create a superuser for Django Admin? (y/n)"
read -r CREATE_SUPER
if [ "$CREATE_SUPER" = "y" ]; then
  python manage.py createsuperuser
fi

echo ""
echo "✅  Setup complete!"
echo "    Run:  source venv/bin/activate && python manage.py runserver"
echo "    Open: http://127.0.0.1:8000"
echo ""
