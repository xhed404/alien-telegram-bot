# 👽 Alien Telegram Bot

Телеграм-бот, который переводит твою речь на "инопланетский" и обратно — с помощью модели Mixtral (через Groq API).

## 🚀 Установка

1. Клонируй репозиторий:
```bash
git clone https://github.com/yourname/alien-telegram-bot.git
cd alien-telegram-bot
```

2. Установи зависимости:
```bash
pip install -r requirements.txt
```

3. Запусти бота:
```bash
python bot.py
```

## 📦 Что используется
- [Groq API](https://console.groq.com/) + модель `mixtral-8x7b-32768`
- Telegram Bot API (через [aiogram](https://docs.aiogram.dev/))

## 🧠 Поведение
- Превращает обычный текст в бред на "инопланетском" языке
- Переводит обратно на человеческий с юмором и ошибками

## 📸 Пример
```text
👤: Привет, кто ты?
👽: Zlorf znak-vish! 🛸⚡️ Blumm grax tor-zik.
🗣: Я прибыл из зоны Z-19. Надеюсь, ты умеешь готовить борщ.
```
