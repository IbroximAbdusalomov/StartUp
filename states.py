from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateUserState(StatesGroup):
    lang = State()
    name = State()
    phone = State()


class CategorysForSell(StatesGroup):
    product_type = State()
    sub_category = State()
    text = State()
    photo = State()
    phone = State()
    status = State()
    id = State()
    name = State()
    created_at = State()
    sell_or_buy = State()


class CategorysForSearch(StatesGroup):
    product_type = State()
    sub_category = State()
    text = State()
    photo = State()
    phone = State()
    status = State()
    id = State()
    name = State()
    created_at = State()
    sell_or_buy = State()


class AddBall(StatesGroup):
    user_id = State()
    ball = State()


class AdminReadNewPostsByData(StatesGroup):
    data = State()


class DElPost(StatesGroup):
    id = State()
    user_id = State()
