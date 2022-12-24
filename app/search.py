from aiogram.dispatcher import FSMContext

from buttons import main_mane_2_uz, main_mane_2_en, sub_category_uz, sub_category_en, main_menu_en, main_menu_uz
from create_bot import db, Dispatcher, bot
from aiogram import types

from messages import Tanlang_uz, Tanlang_en
from states import CategorysForSearch
from app.func_ import check_lan_and_btn


async def start_category(callback: types.CallbackQuery):
    await CategorysForSearch.product_type.set()
    await check_lan_and_btn(callback.from_user.id, Tanlang_uz, Tanlang_en, main_mane_2_uz(), main_mane_2_en())


async def category_1(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['product_type'] = callback.data
        await check_lan_and_btn(callback.from_user.id, Tanlang_uz, Tanlang_en, sub_category_uz(), sub_category_en())
    await CategorysForSearch.next()


async def category_2(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['sub_category'] = callback.data

        post = db.search_posts(category_1=data.get('product_type'), category_2=data.get('sub_category'))
        if post:
            for i in post:
                await bot.send_photo(callback.from_user.id, i[2], f"""Description: {i[7]}\n {i[5]}\n #{i[6]}""")
            await check_lan_and_btn(callback.from_user.id, Tanlang_uz, Tanlang_en, main_menu_uz(), main_menu_en())
        else:
            await check_lan_and_btn(callback.from_user.id, "E'lon topilmadi", "Post not found", main_menu_uz(),
                                    main_menu_en())
    await state.finish()


def register_search(dp: Dispatcher):
    dp.register_callback_query_handler(start_category, text='search')
    dp.register_callback_query_handler(category_1, text=['used', 'new', 'raw material', 'frame'],
                                       state=CategorysForSearch.product_type)
    dp.register_callback_query_handler(category_2, text=['agro', 'tekstil', 'metal', 'mebel', 'plastik'],
                                       state=CategorysForSearch.sub_category)
