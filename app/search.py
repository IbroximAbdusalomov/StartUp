from aiogram.dispatcher import FSMContext

from buttons import main_mane_2_uz, main_mane_2_en, sub_category_uz, sub_category_en
from create_bot import db, Dispatcher, bot
from aiogram import types

from messages import Tanlang_uz, Tanlang_en
from states import CategorysForSearch
from func_ import check_lan_and_btn


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
                await bot.send_photo(callback.from_user.id, text=f"""{i[2]}\n{i[7]}\n{i[5]}\n{i[6]}""")


def register_search(dp: Dispatcher):
    dp.register_callback_query_handler(start_category, text='search')
