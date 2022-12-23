from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from buttons import phone, choice_lang, main_menu_en, main_menu_uz
from messages import uz_name, en_name, uz_phone, en_phone, uz_name_wrong, en_name_wrong, uz_register, en_registerd, \
    Tanlang_uz, Tanlang_en
from states import CreateUserState
from create_bot import bot, db, Dispatcher
from app.func_ import check_lan_and_btn, check_lan


async def main_send_welcome(message: types.Message):
    if not db.user_exists(message.from_user.id):
        await bot.send_message(message.from_user.id,
                               "*Choose lanuage:\n"
                               "----------\n"
                               "Tilni tanlang:*", parse_mode='markdown', reply_markup=choice_lang())
        await CreateUserState.lang.set()
    else:
        await check_lan_and_btn(message.from_user.id, Tanlang_uz, Tanlang_en, main_menu_uz(), main_menu_en())


# -----------------------------------------------------------------------------------------------------------------------

async def choice_language(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if callback.data == "uz":
            await callback.message.delete()
            data['lan'] = callback.data
            await bot.send_message(callback.from_user.id, uz_name, parse_mode='markdown')
            await CreateUserState.name.set()
        elif callback.data == "en":
            await callback.message.delete()
            data['lan'] = callback.data
            await bot.send_message(callback.from_user.id, en_name, parse_mode='markdown')
            await CreateUserState.name.set()


# -----------------------------------------------------------------------------------------------------------------------

async def main(message: types.Message, state: FSMContext = None):
    async with state.proxy() as data:
        if message.content_type == 'text' and message.text != "/start":
            data['name'] = message.text
            if data.get('lan') == 'uz':
                await message.answer(uz_phone, reply_markup=phone())
                await CreateUserState.phone.set()
            else:
                await message.answer(en_phone, reply_markup=phone())
                await CreateUserState.phone.set()
        else:
            if data.get('lan') == 'uz':
                await message.answer(uz_name_wrong)
                await CreateUserState.name.set()
            else:
                await message.answer(en_name_wrong)
                await CreateUserState.name.set()


# -----------------------------------------------------------------------------------------------------------------------


async def phone_(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.content_type == 'contact':
            number = message.contact['phone_number']
            if number.startswith('+998') or number.startswith('998'):
                db.add_user(message.from_user.id, data.get('name'), number, data.get('lan'))
                if data.get('lan') == 'uz':
                    await message.answer(uz_register, reply_markup=main_menu_uz())
                    await CreateUserState.phone.set()
                else:
                    await message.answer(en_registerd, reply_markup=main_menu_en())
                    await CreateUserState.phone.set()
            await state.finish()
        else:
            if data.get('lan') == 'uz':
                await message.answer(uz_phone, reply_markup=phone())
                await CreateUserState.phone.set()
            else:
                await message.answer(en_phone, reply_markup=phone())
                await CreateUserState.phone.set()


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(main_send_welcome, commands=['start', 'help'])

    dp.register_callback_query_handler(choice_language, state=CreateUserState.lang)

    dp.register_message_handler(main, state=CreateUserState.name, content_types=ContentType.ANY)

    dp.register_message_handler(phone_, state=CreateUserState.phone, content_types=ContentType.ANY)
