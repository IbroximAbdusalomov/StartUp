from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

from database import DataBase

API_TOKEN = '5846618049:AAG9qpx1jFee4E26RtCvwt9pI2bBYFINhpY'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = DataBase('database.sqlite')
