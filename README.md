# 🧾 TaxBerry

**Modular tax & accounting dashboard for Raspberry Pi**  
Open-source, privacy-friendly and built for freelancers, clubs, and crypto investors.

---

## 🔍 About

**TaxBerry** is a lightweight Django-based backend for local tax tools and accounting workflows.  
Designed to run on **Raspberry Pi** devices, it offers full control over sensitive financial data without relying on cloud services.

Use cases include:

- 💼 Freelancers and self-employed professionals
- 🌿 Cannabis Social Clubs (under KCanG regulations)
- 🧮 Crypto portfolio tax tracking
- 📦 Verein administration (e.g. member fees, assets)

---

## 🧱 Tech Stack

- **Backend:** Django 5.x + Django REST Framework
- **Frontend:** Coming soon – React + Vite
- **Environment:** Runs on Raspberry Pi OS (Debian-based)
- **Privacy:** Fully GDPR-compliant, no external analytics, zero third-party tracking

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/saschadaemgen/taxberry.git
cd taxberry
```

### 2. Create and activate virtual environment (Windows)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Django development server

```bash
cd backend
python manage.py runserver
```

Server will be available at:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🐍 Requirements

Python 3.10+  
Raspberry Pi OS (Bullseye or newer recommended)

> See `requirements.txt` for all Python packages.

---

## 🛡️ Security & Privacy

- 100% local execution (no cloud dependency)
- Zero telemetry, no tracking, no cookies
- Compatible with self-hosted VPNs, firewalls, and air-gapped environments

---

## 🔧 Project Structure

```
taxberry/
├── .venv/              # Virtual environment
├── backend/            # Django backend
│   ├── manage.py
│   └── taxberry/
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── ...
├── requirements.txt
└── README.md
```

---

## 📌 Roadmap

- [x] Backend bootstrapped with Django
- [ ] Frontend React dashboard (with Pi touch UI support)
- [ ] CSV / XML export for tax office
- [ ] Crypto wallet import (read-only)
- [ ] NFC support for secure member login
- [ ] Offline PDF invoicing / receipt printing

---

## 🤝 Contributing

Coming soon – all contributions will follow a modular plugin structure with per-feature GitHub issues.

---

## 📜 License

MIT License – see `LICENSE` file for details.

---

## 🌐 Official Website

Coming soon: [https://tax-berry.com](https://tax-berry.com)  
(also available under: [https://steuer-berry.de](https://steuer-berry.de))

---

> Made with 🍓 and 🧾 on a Raspberry Pi by Sascha Dämgen IT and More
