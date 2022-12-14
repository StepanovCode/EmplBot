import os
from dotenv import load_dotenv, find_dotenv

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv(find_dotenv())

bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
