from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateUserState(StatesGroup):
    lang = State()
    name = State()
    phone = State()


class InsetProduct(StatesGroup):
    product_type = State()
    photo = State()
    decription = State()
    category = State()  # sub category
    user_id = State()
    user_name = State()
    created_at = State()


class CategorysForSearch(StatesGroup):
    product_type = State()
    sub_category = State()


class AddBall(StatesGroup):
    user_id = State()
    ball = State()


class Admin(StatesGroup):
    data = State()
