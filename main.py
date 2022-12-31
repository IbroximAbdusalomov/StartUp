import logging
from aiogram import executor, types

from app.func_ import check_lan_and_btn
from app.mycobinet.mycobinet import register_mycb
from app.search_me import register_search
from buttons import mycb_uz, mycb_en
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


# @dp.message_handler(content_types=['photo'])
# async def start(msg: types.Message):
#     # markup = InlineKeyboardMarkup().add(InlineKeyboardButton("text", callback_data="cd"))
#     if "sendall" in msg.caption:
#         await msg.answer_photo(photo=msg.photo[-1].file_id, caption=msg.caption[9:])
#
#         # await bot.send_photo(chat_id=msg.chat.id, photo=msg.photo[-1].file_id, caption=msg.caption, reply_markup=markup)


# @dp.callback_query_handler(text='mypr')
# async def mypr(callback: types.CallbackQuery):
#     await check_lan_and_btn(callback.from_user.id, "Hush kelibsiz", "Welcome", mycb_uz(), mycb_en())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
