from aiogram import types

from app.func_ import check_lan_and_btn
from buttons import main_menu_uz, main_menu_en
from create_bot import db, bot, Dispatcher


async def my_posts(callback: types.CallbackQuery):
    my_post = db.my_posts(callback.from_user.id)
    if my_post:
        for i in my_post:
            await bot.send_photo(callback.from_user.id, i[2],
                                 f'ID:{i[3]}\nDescription: {i[7]}\n{i[5]}\n#{i[6]}')
    else:
        await check_lan_and_btn(callback.from_user.id, "E'lon topilmadi", "Post not found", main_menu_uz(),
                                main_menu_en())


async def my_profile(query: types.CallbackQuery):
    user = db.select_user(query.from_user.id).fetchall()
    for i in user:
        await bot.send_message(query.from_user.id,
                               f'ID🆔: {i[3]}\nUsername👤: {i[2]}\nPhone☎️: {i[4]}\nBall 💸:{i[5]}\nLang🇺🇿🇬🇧: {i[7]}')


def register_mycb(dp: Dispatcher):
    dp.register_callback_query_handler(my_posts, text=['mypost'])
    dp.register_callback_query_handler(my_profile, text=['myprofil'])
