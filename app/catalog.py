from aiogram import Dispatcher
from aiogram.types import ChatActions

from app.func_ import check_lan
from create_bot import bot


async def show_products(m, products):
    if len(products) == 0:
        await check_lan(m.chat.id, 'Hech nima toplimadi', 'Nothing found')
    else:
        await bot.send_chat_action(m.chat.id, ChatActions.TYPING)

        for idx, title, body, image, price, _ in products:
            text = f'<b>{title}</b>\n\n{body}'

            await m.answer_photo(photo=image, caption=text)


def register_search(dp: Dispatcher):
    dp.register_callback_query_handler(show_products, text='search')