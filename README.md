# Telegram Bot Storage

A Telegram bot to store notes, documents, images, and videos using Python, Poetry, and PostgreSQL. This open-source project helps you save various file types securely and access them anytime via Telegram.

---

## Features

- Store text notes, PDFs, docs, images, videos, and other files
- PostgreSQL database for persistent storage
- Built with python-telegram-bot, SQLAlchemy, and Poetry
- Easy setup and deployment

---

## Requirements

- Python 3.10+
- PostgreSQL
- Poetry

---

## Setup Instructions
```
### 1. Clone the repository
git clone https://github.com/your-username/telegram-bot-storage.git
cd telegram-bot-storage

---

### Install Poetry
poetry install

---

### Create a .env file in the project root with the following content: 
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/telegram_bot_db

---

### Run the bot
python bot.py
