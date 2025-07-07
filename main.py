import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню
def get_main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("🚢 Типы судов"))
    keyboard.add(KeyboardButton("💬 Мотивация моряку"))
    keyboard.add(KeyboardButton("📬 Совет дня"))
    keyboard.add(KeyboardButton("🧠 Морской тест"))
    return keyboard

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply(
        "Приветствую, моряк! 🌊\nЭтот бот поможет тебе прокачаться в морской теме!",
        reply_markup=get_main_menu()
    )

@dp.message_handler(lambda message: message.text == "💬 Мотивация моряку")
async def send_motivation(message: types.Message):
    phrases = [
        "Каждый моряк — сам себе капитан! ⛵",
        "Штормы делают тебя сильнее! 🌪️",
        "Покой нам только снится — в море ты живёшь по-настоящему! ⚓",
        "Держи курс и не сворачивай, брат! 🌍"
    ]
    await message.reply(random.choice(phrases))

@dp.message_handler(lambda message: message.text == "📬 Совет дня")
async def send_tip(message: types.Message):
    tips = [
        "Перед вахтой всегда проверяй снаряжение.",
        "Сохраняй спокойствие в любой ситуации.",
        "Всегда уважай старших по званию и помогай младшим.",
        "Держи форму — тело моряка должно быть крепким!"
    ]
    await message.reply(random.choice(tips))

@dp.message_handler(lambda message: message.text == "🚢 Типы судов")
async def ship_types(message: types.Message):
    await message.reply(
        "Вот несколько типов судов:\n\n"
        "🛳️ Круизный лайнер — для пассажиров\n"
        "🚢 Контейнеровоз — для грузов\n"
        "⛴️ Паром — перевозит людей и машины\n"
        "🛥️ Яхта — для отдыха\n"
        "⚓ Танкер — для нефти и топлива"
    )

@dp.message_handler(lambda message: message.text == "🧠 Морской тест")
async def marine_quiz(message: types.Message):
    question = "Сколько вахт в морских сутках?"
    options = ["2", "3", "4", "6"]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for option in options:
        keyboard.add(KeyboardButton(option))
    await message.reply(question, reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in ["2", "3", "4", "6"])
async def handle_answer(message: types.Message):
    if message.text == "4":
        await message.reply("✅ Верно! В сутках 4 вахты по 6 часов.")
    else:
        await message.reply("❌ Неверно. Правильный ответ — 4.")

if __name__ == "__main__":
    import random
    executor.start_polling(dp, skip_updates=True)