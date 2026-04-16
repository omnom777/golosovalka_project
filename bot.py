import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
PROXY_URL = os.getenv("PROXY_URL")

if not TOKEN:
    raise ValueError("Не найден BOT_TOKEN в .env")

dp = Dispatcher()


@dp.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)


async def main():
    if PROXY_URL:
        session = AiohttpSession(proxy=PROXY_URL)
        bot = Bot(token=TOKEN, session=session)
    else:
        bot = Bot(token=TOKEN)

    me = await bot.get_me()
    print(f"Бот запущен: @{me.username}")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())