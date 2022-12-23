import logging
from aiogram import executor

from app.catalog import register_search
from create_bot import dp
from app.sell import regiter_handler_sell
from app.start import register_handler_start

logging.basicConfig(level=logging.INFO)
register_search(dp)
regiter_handler_sell(dp)
register_handler_start(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
