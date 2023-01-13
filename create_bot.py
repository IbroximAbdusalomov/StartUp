import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

from database import DataBase
logging.basicConfig(level=logging.INFO)
API_TOKEN = 'Your TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = DataBase('database.sqlite')
