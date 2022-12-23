import logging
from aiogram import types, executor
from create_bot import dp

logging.basicConfig(level=logging.INFO)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
