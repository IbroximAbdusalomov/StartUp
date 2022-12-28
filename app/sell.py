from datetime import datetime
from aiogram import types
from buttons import main_mane_2_uz, main_mane_2_en, sub_category_uz, sub_category_en, main_menu_uz, main_menu_en
from create_bot import Dispatcher, db, bot
from app.func_ import check_lan, check_lan_and_btn
from states import InsetProduct
from messages import Tanlang_uz, Tanlang_en, image_uz, image_en, desc_uz, desc_en
from aiogram.dispatcher import FSMContext


async def sell_product_1(callback: types.CallbackQuery):
    await InsetProduct.product_type.set()
    await check_lan_and_btn(callback.from_user.id, Tanlang_uz, Tanlang_en, main_mane_2_uz(), main_mane_2_en())


# add product_type
async def sell_product_2(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['product_type'] = callback.data
    await InsetProduct.next()
    await check_lan(callback.from_user.id, image_uz, image_en)

    # add photo


# dp.register_message_handler(load_photo, content_types=['photo'], state=Inset_Product_1.photo)
async def sell_product_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await check_lan(message.from_user.id, desc_uz, desc_en)
    await InsetProduct.next()


async def sell_product_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if len(message.text) <= 250:
            data['decription'] = message.text
            await check_lan_and_btn(message.from_user.id, Tanlang_uz, Tanlang_en, sub_category_uz(), sub_category_en())
        else:
            await message.answer("Text bilan xatolik")
    await InsetProduct.next()


async def sell_product_5(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = callback.data
        data['user_id'] = callback.from_user.id
        data['user_name'] = callback.from_user.full_name
        data['created_at'] = datetime.strftime(datetime.now(), '%Y-%m-%d')
    if db.coin(callback.from_user.id):
        db.add_product(data.get('created_at'), data.get('photo'), data.get('user_id'),
                       data.get('user_name'), data.get('product_type'), data.get('category'), data.get('decription'))
        await check_lan_and_btn(callback.from_user.id, "'Xabar qo'shildi'", "Dd was added", main_menu_en(),
                                main_menu_en())
    else:
        pass

        # await check_lan_and_btn(callback.from_user.id,
        #                         """Sizda ball kam!\n/help <- bosing qo'shimcha malumotlar chiqadi""", "You ball 0 ",
        #                         main_menu_uz())

    await state.finish()


def regiter_handler_sell(dp: Dispatcher):
    dp.register_callback_query_handler(sell_product_1, text=['cell'])
    dp.register_callback_query_handler(sell_product_2, state=InsetProduct.product_type)
    dp.register_message_handler(sell_product_3, content_types='photo', state=InsetProduct.photo)
    dp.register_message_handler(sell_product_4, state=InsetProduct.decription)
    dp.register_callback_query_handler(sell_product_5, text=['agro', 'tekstil', 'metal', 'mebel', 'plastik'],
                                       state=InsetProduct.category)
