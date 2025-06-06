import os
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def call_groq(messages):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": messages,
        "temperature": 1.2
    }
    response = requests.post(GROQ_URL, json=data, headers=headers)
    return response.json()['choices'][0]['message']['content']

@dp.message_handler()
async def alien_chat(message: types.Message):
    user_text = message.text

    alien_msg = call_groq([
        {"role": "system", "content": "Ты говоришь как инопланетянин с эмодзи, странными словами и звуками."},
        {"role": "user", "content": user_text}
    ])

    human_translation = call_groq([
        {"role": "system", "content": "Ты человек-лингвист. Пробуешь перевести инопланетную фразу на человеческий язык, но иногда ошибаешься или додумываешь."},
        {"role": "user", "content": alien_msg}
    ])

    await message.answer(f"👽: {alien_msg}\n\n🗣: {human_translation}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
