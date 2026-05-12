# 😄 Telegram Joke Bot

An asynchronous Telegram bot that delivers hilarious Chuck Norris jokes. The bot uses a modern Python stack with async/await and integrates with a public API.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-v7.0%2B-blue?style=for-the-badge&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🛠️ Tech Stack

- **python-telegram-bot** — official library for Telegram Bot API
- **aiohttp** — asynchronous HTTP client for API requests
- **python-dotenv** — environment variable management

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/telegram-joke-bot.git
cd telegram-joke-bot
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
TOKEN=your_telegram_token_from_botfather
```

> 💡 **How to get a token?**
> 1. Open Telegram and find the **@BotFather** bot
> 2. Send the `/newbot` command
> 3. Follow the instructions and copy your token

### 5. Run the bot

```bash
python main.py
```

## 📱 Usage

1. Open Telegram and find your bot
2. Send the `/start` command
3. Click the "Get a joke" button
4. Enjoy a random Chuck Norris joke! 😂

## 📖 Documentation

- [python-telegram-bot Documentation](https://python-telegram-bot.readthedocs.io/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Chuck Norris API](https://api.chucknorris.io/)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
