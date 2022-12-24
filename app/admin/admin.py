from aiogram import types
from aiogram.dispatcher import FSMContext

from app.func_ import check_lan
from create_bot import db, Dispatcher, bot
from states import AddBall


# -------------------------Add ball------------------------------------------------------------------------

async def addball(message: types.Message):
    await AddBall.user_id.set()
    await check_lan(message.from_user.id, "Userni idsini jo'nating", "send message user id")


async def step_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # user_id = db.get_users()
        if message.text in db.all_users(message.text):
            data['user_id'] = message.text
            await check_lan(message.from_user.id, "Qancha qo'shilsin ?", "How much to add ?")
        else:
            await check_lan(message.from_user.id, "Id topilmadi ?", "Id not found")
    await AddBall.next()


async def step_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ball'] = message.text
        db.set_ball(data.get('user_id'), data.get('ball'))
    await state.finish()
    await bot.send_message(message.from_user.id, "Added")


# --------------------------------sendall text рацылка V-1-----------------------------------------------------------------


# @dp.message_handler(commands='sendall')
async def selndall(message: types.message):
    if message.chat.type == "private":
        text = message.text[9:]
        admin = db.all_users(message.from_user.id)
        if admin[6] == "ADMIN":
            # await message.answer('Start')
            for i in db.get_users():
                try:
                    await bot.send_message(i[0], text)
                    print('Send text all users')
                except:
                    await check_lan(message.from_user.id, "User yo'q", "Users not found")
        else:
            await bot.send_message(message.from_user.id, "Command not found")


# --------------------------------sendall text рацылка V-2-----------------------------------------------------------------

# @dp.message_handler(content_types=['photo'])
# async def V2(msg: types.Message):
#     admin = db.all_users(msg.from_user.id)
#     if "sendall" in msg.caption and admin[6] == "ADMIN":
#         for i in db.get_users():
#             await bot.send_photo(i[3], photo=msg.photo[-1].file_id, caption=msg.caption[9:])


# ---------------------------Statistika----------------------------------------------------------------------

# async def statistika(message: types.Message):
#     users = db.get_users()
#     if db.all_users(message.from_user.id)[6] == "ADMIN":
#         for i in users:
#             await bot.send_message(message.from_user.id, "")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(addball, commands='addball')
    dp.register_message_handler(step_1, state=AddBall.user_id)
    dp.register_message_handler(step_2, state=AddBall.ball)

    dp.register_message_handler(selndall, commands='sendall')

    # dp.register_message_handler(V2, content_types=['photo'])
