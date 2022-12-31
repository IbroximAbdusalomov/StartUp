import logging
from aiogram import executor
from app.mycobinet.mycobinet import register_mycb
from app.search_me import register_search
from create_bot import dp
from app.sell import regiter_handler_sell
from app.start import register_handler_start
from app.admin.admin import register_admin

logging.basicConfig(level=logging.INFO)

"""   Register handlers   """
regiter_handler_sell(dp)
register_handler_start(dp)
register_search(dp)
register_mycb(dp)
register_admin(dp)
"""        THE END        """

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
