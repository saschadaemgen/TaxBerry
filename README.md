# TaxBerry

**Multilingual Accounting Software for Raspberry Pi and Web**

TaxBerry is a privacy-first, multilingual accounting system designed for clubs, cooperatives, and individual use.  
Optimized for deployment on low-resource devices like the Raspberry Pi, but scalable to full web environments.

---

## 🚀 Features

- 🌍 Multilingual user interface
- 📦 Modular backend with Django
- 💾 Offline-capable (Raspberry Pi support)
- 🔐 Zero cloud dependency – fully self-hosted
- 🧾 Simplified tax calculation logic
- 📊 Exportable reports and analytics
- ⚙️ API-first design for frontend integrations

---

## 📦 Tech Stack

| Layer        | Stack                      |
|-------------|----------------------------|
| Backend      | Django (Python)            |
| Frontend     | (Planned) React / PWA      |
| Database     | SQLite / PostgreSQL        |
| Deployment   | Raspberry Pi / Docker / Web |
| Language     | Python 3.12+               |

---

## 🛠️ Development Setup

```bash
# 1. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# 2. Install Django
pip install django

# 3. Start development server
cd backend
python manage.py runserver