from aiogram import types
from aiogram.dispatcher import FSMContext

from app.func_ import check_lan
from buttons import btn_for_admin
from create_bot import db, Dispatcher, bot
from states import AddBall, AdminReadNewPostsByData


async def admin(message: types.Message):
    await bot.send_message(message.from_user.id, "Welcome admin", reply_markup=btn_for_admin())


# -------------------------------------send all-------------------------------------------------------

async def addball(message: types.Message):
    await AddBall.user_id.set()
    await check_lan(message.from_user.id, "Userni idsini jo'nating", "send message user id")


async def step_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = db.user_exists(message.from_user.id)
        if user_id:
            data['user_id'] = message.text
            await check_lan(message.from_user.id, "Qancha qo'shilsin ?", "How much to add ?")
        else:
            await check_lan(message.from_user.id, "Id topilmadi ?", "Id not found")
            await state.finish()
    await AddBall.next()


async def step_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ball'] = message.text
        ball = db.user_exists(data.get('user_id'))
        db.set_ball(data.get('user_id'), data.get('ball'))
    await state.finish()
    await bot.send_message(message.from_user.id, "Added", reply_markup=btn_for_admin())


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

        else:
            await bot.send_message(message.from_user.id, "Command not found")


# -------------------------------------read new posts by data-------------------------------------------------------

async def read_new_posts(callback: types.CallbackQuery):
    await AdminReadNewPostsByData.data.set()
    await bot.send_message(callback.from_user.id, "Send data")


async def read_new_posts_step_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['data'] = message.text
        result = db.new_posts(data.get('data'))
        if result:
            for i in result:
                await bot.send_photo(message.from_user.id, i[2],
                                     f"""ID: {i[0]}\nCreate at: {i[1]}\nUser id: {i[3]}\nUsername: {i[4]}\nDescription: {i[7]}\nCategory 1: {i[5]}\nCategory 2: {i[6]}""")
            await message.answer("Menu", reply_markup=btn_for_admin())
        else:
            await message.answer("Post not found")


# --------------------------------------------------------------------------------------------

async def add_admin(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, "Userni idsini jo'nating")


async def add_admin_1(message: types.Message):
    try:
        db.dbaddadmin(message.text)
        await bot.send_message(message.from_user.id, "Sucses")
    except:
        await bot.send_message(message.from_user.id, "Id xato")


# --------------------------------------------------------------------------------------------

def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin, commands='admin')
    dp.register_callback_query_handler(addball, text='addball')
    dp.register_message_handler(step_1, state=AddBall.user_id)
    dp.register_message_handler(step_2, state=AddBall.ball)

    dp.register_message_handler(selndall, commands='sendall')

    dp.register_callback_query_handler(read_new_posts, text='newposts')
    dp.register_message_handler(read_new_posts_step_1, state=AdminReadNewPostsByData.data)
    dp.register_callback_query_handler(add_admin, text='addadmin')
    dp.register_message_handler(add_admin_1)
