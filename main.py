from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
from aiogram.filters.command import CommandStart
import os
from config import BOT_TOKEN


if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in config")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Hello ! Welcome to the bot.")

@dp.message(Command("music"))
async def music_handler(message: Message):
    await message.answer("Playing music...")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



