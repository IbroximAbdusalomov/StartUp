import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

from database import DataBase
logging.basicConfig(level=logging.INFO)
API_TOKEN = '5663518655:AAHTdZh4HaQRfRTKaykpFDkYhNy6YajLUN4'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = DataBase('database.sqlite')
