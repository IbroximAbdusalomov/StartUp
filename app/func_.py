from create_bot import db, bot


async def check_lan(id, text_uz, text_en):
    if db.chek_user_lang(id) == "uz":
        await bot.send_message(id, text=text_uz)
    elif db.chek_user_lang(id) == "en":
        await bot.send_message(id, text=text_en)


async def check_lan_and_btn(id, text_uz, text_en, btn_uz, btn_en):
    if db.check_user_lang(id) == "uz":
        await bot.send_message(id, text=text_uz, reply_markup=btn_uz)
    elif db.check_user_lang(id) == "en":
        await bot.send_message(id, text=text_en, reply_markup=btn_en)
