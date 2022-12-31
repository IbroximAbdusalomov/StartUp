from aiogram import types

from app.func_ import check_lan_and_btn
from buttons import main_menu_uz, main_menu_en, btn_for_delete_post
from create_bot import db, bot, Dispatcher
from messages import Tanlang_uz, Tanlang_en


async def my_posts(callback: types.CallbackQuery):
    my_post = db.my_posts(callback.from_user.id)
    if my_post:
        for i in my_post:
            await bot.send_photo(callback.from_user.id, i[2],
                                 f'ID:{i[0]}USER\nID:{i[3]}\nDescription: {i[7]}\n{i[5]}\n#{i[6]}')
        await bot.send_message(callback.from_user.id, "Delete", reply_markup=btn_for_delete_post())
        await check_lan_and_btn(callback.from_user.id, "Menu", "Menu", main_menu_uz(),
                                main_menu_en())

    else:
        await check_lan_and_btn(callback.from_user.id, "E'lon topilmadi", "Post not found", main_menu_uz(),
                                main_menu_en())


async def my_profile(callback: types.CallbackQuery):
    user = db.all_users(callback.from_user.id)
    for i in user:
        await bot.send_message(callback.from_user.id,
                               f'ID🆔: {i[3]}\nUsername👤: {i[2]}\nPhone☎️: {i[4]}\nBall 💸:{i[5]}\nLang🇺🇿🇬🇧: {i[7]}')
    await check_lan_and_btn(callback.from_user.id, Tanlang_uz, Tanlang_en, main_menu_uz(), main_menu_en())


async def delete_post_0(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, "Po'stni idsini jo'nating")


async def delete_post_1(message: types.Message):
    try:
        db.del_post(message.text, message.from_user.id)
    except:
        await bot.send_message(message.from_user.id, "Id xato")


def register_mycb(dp: Dispatcher):
    dp.register_callback_query_handler(my_posts, text='mypost')
    dp.register_callback_query_handler(my_profile, text='myprofil')
    dp.register_callback_query_handler(delete_post_0, text='del')
    dp.register_message_handler(delete_post_1)
