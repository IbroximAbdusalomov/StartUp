from aiogram import types
from aiogram.dispatcher import FSMContext

from app.func_ import check_lan
from create_bot import db, Dispatcher, bot
from states import AddBall


# -------------------------------------send all-------------------------------------------------------

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


# -------------------------------------send all-------------------------------------------------------
async def selndall(message: types.message):
    if message.chat.type == "private":
        text = message.text[9:]
        admin = db.all_users(message.from_user.id)
        if admin[6] == "ADMIN":
            for i in db.get_users():
                try:
                    await bot.send_message(i[3], text)
                except:
                    await check_lan(message.from_user.id, "User yo'q", "Users not found")
        # print('Send text all users')

        else:
            await bot.send_message(message.from_user.id, "Command not found")


# -------------------------------------read new posts by data-------------------------------------------------------

# --------------------------------------------------------------------------------------------

def register_admin(dp: Dispatcher):
    dp.register_message_handler(addball, commands='addball')
    dp.register_message_handler(step_1, state=AddBall.user_id)
    dp.register_message_handler(step_2, state=AddBall.ball)

    dp.register_message_handler(selndall, commands='sendall')

    # dp.register_callback_query_handler(ReadNewPost, text='newposts') #by data
