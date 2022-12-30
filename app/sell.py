from datetime import datetime
from aiogram import types
from aiogram.types import ContentType

from buttons import main_mane_2_uz, main_mane_2_en, sub_category_uz, sub_category_en, phone_en, phone_uz, btn_yes_no, \
    main_menu_en, main_menu_uz
from create_bot import Dispatcher, db, bot
from app.func_ import check_lan, check_lan_and_btn
from states import CategorysForSell
from messages import Tanlang_uz, Tanlang_en
from aiogram.dispatcher import FSMContext


async def sell_category_0(callback: types.CallbackQuery):
    await CategorysForSell.product_type.set()
    await check_lan_and_btn(callback.from_user.id, Tanlang_uz, Tanlang_en, main_mane_2_uz(), main_mane_2_en())


# Ishlatilgan
async def category_1(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['sell_or_buy'] = 'SELL'
        data['product_type'] = callback.data
        await check_lan_and_btn(callback.from_user.id, Tanlang_uz, Tanlang_en, sub_category_uz(), sub_category_en())
    await CategorysForSell.next()


async def sell_category_2(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['sub_category'] = callback.data
        await check_lan(callback.from_user.id, "Ma'lumot qoldiring", "Send description")
    await CategorysForSell.next()


async def sell_category_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        await check_lan(message.from_user.id, "Rasmini jo'nating", "Send photo")
    await CategorysForSell.next()


async def sell_category_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await check_lan_and_btn(message.from_user.id, "Telefon raqamingizni jo'nating", "Send phone number",
                                phone_uz(),
                                phone_en())
    await CategorysForSell.next()


async def sell_category_5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.content_type == 'contact':
            number = message.contact['phone_number']
            if number.startswith('+998') or number.startswith('998'):
                data['phone'] = number
                data['status'] = 'no'
                data['id'] = message.from_user.id
                data['name'] = message.from_user.full_name
                data['created_at'] = datetime.strftime(datetime.now(), '%Y-%m-%d')
                await bot.send_photo(message.from_user.id, data['photo'],
                                     f"Category 1:#{data.get('product_type')}\nCategory 2:#{data.get('sub_category')}\nDescripton:{data.get('text')}\nPhone number:{data.get('phone')}\nName:{data.get('name')}\n{data.get('sell_or_buy')}",
                                     reply_markup=btn_yes_no())
    await CategorysForSell.next()


async def sell_category_6(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if db.coin(callback.from_user.id):
            data['status'] = callback.data
            await bot.send_photo('@TESt_my_bo', data['photo'],
                                 f"Category 1:#{data.get('product_type')}\nCategory 2:#{data.get('sub_category')}\nDescripton:{data.get('text')}\nPhone number:{data.get('phone')}\nName:{data.get('name')}\n{data.get('sell_or_buy')}")
            await check_lan_and_btn(callback.from_user.id, "Menyu", "Manu", main_menu_uz(), main_menu_en())
            db.add_product(data.get('created_at'), data.get('photo'), data.get('id'), data.get('name'),
                           data.get('product_type'), data.get('sub_category'), data.get('text'),
                           data.get('sell_or_buy'))
    await state.finish()

def regiter_handler_sell(dp: Dispatcher):
    dp.register_callback_query_handler(sell_category_0, text=['cell', 'no'])
    dp.register_callback_query_handler(category_1, text=['used', 'new', 'raw material', 'frame'],
                                       state=CategorysForSell.product_type)
    dp.register_callback_query_handler(sell_category_2, text=['agro', 'tekstil', 'metal', 'mebel', 'plastik'],
                                       state=CategorysForSell.sub_category)
    dp.register_message_handler(sell_category_3, state=CategorysForSell.text)
    dp.register_message_handler(sell_category_4, content_types=['photo'], state=CategorysForSell.photo)
    dp.register_message_handler(sell_category_5, content_types=ContentType.ANY, state=CategorysForSell.phone)
    dp.register_callback_query_handler(sell_category_6, text=['yes'], state=CategorysForSell.status)
