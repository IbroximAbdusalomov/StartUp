import logging
from aiogram import types, executor

from app.catalog import register_search
from create_bot import dp

logging.basicConfig(level=logging.INFO)
register_search(dp)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
