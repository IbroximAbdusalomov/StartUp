from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# btn_menu = KeyboardButton("/Menu")

number_uz = KeyboardButton("Telefon raqamni jo‘natish", request_contact=True)
number_en = KeyboardButton("SEnd phone number", request_contact=True)

uzb_lang = InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data='uz')
en_lang = InlineKeyboardButton("🇺🇸 English", callback_data='en')

# uz
search_inl = InlineKeyboardButton("🔎 Qidirish", callback_data='search')
cell_inl = InlineKeyboardButton("🛍 Sotish", callback_data='cell')

# en
search = InlineKeyboardButton("🔎 Search", callback_data='search')
cell = InlineKeyboardButton("🛍 Sell", callback_data='cell')

# uz
ishlatilgan = InlineKeyboardButton("🔎 Ishlatilgan", callback_data='used')
yangi = InlineKeyboardButton("🆕 Yangi", callback_data='new')
xomashyo = InlineKeyboardButton("🔩 Xom ashyo", callback_data='raw material')
kadr = InlineKeyboardButton("👤 Kadr", callback_data='frame')

# en
ishlatilgani = InlineKeyboardButton("🔎 Used", callback_data='used')
yangii = InlineKeyboardButton("🆕 New", callback_data='new')
xomashyoi = InlineKeyboardButton("🔩 Raw material", callback_data='raw material')
kadri = InlineKeyboardButton("👤 Frame", callback_data='frame')

# uz
agro = InlineKeyboardButton("Agro", callback_data='agro')
tekstil = InlineKeyboardButton("Tekstil", callback_data='tekstil')
metal = InlineKeyboardButton("Metal", callback_data='metal')
mebel = InlineKeyboardButton("Mebel", callback_data='mebel')
plastik = InlineKeyboardButton("Plastik", callback_data='plastik')

# en
agroi = InlineKeyboardButton("Agro", callback_data='agro')
tekstili = InlineKeyboardButton("Textile", callback_data='tekstil')
metali = InlineKeyboardButton("Metal", callback_data='metal')
mebeli = InlineKeyboardButton("Furniture", callback_data='mebel')
plastiki = InlineKeyboardButton("Plastic", callback_data='plastik')

my_posts_uz = InlineKeyboardButton(text="📨Mening e'lonlarim", callback_data='mypost')
my_profil_uz = InlineKeyboardButton(text="💼Mening profilm", callback_data='myprofil')

my_posts_en = InlineKeyboardButton(text="📨My posts", callback_data='mypost')
my_profil_en = InlineKeyboardButton(text="💼My profile", callback_data='myprofil')

btn_add_ball = InlineKeyboardButton(text='➕Add ball', callback_data='addball')
btn_new_post = InlineKeyboardButton(text='🆕New posts', callback_data='newposts')
btn_add_admin = InlineKeyboardButton(text='Add admin', callback_data='addadmin')

btn_yes = InlineKeyboardButton(text='☑ Yes', callback_data='yes')
btn_no = InlineKeyboardButton(text='⛔ No', callback_data='no')

btnphone_uz = KeyboardButton("Telefon raqamingizni jo'nating", request_contact=True)
btnphone_en = KeyboardButton("Send phone number", request_contact=True)

btn_delete = InlineKeyboardButton(text='🗑️ Delete', callback_data='del')


def mycb_uz():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(my_posts_uz, my_profil_uz)
    return markup


def mycb_en():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(my_posts_en, my_profil_en)
    return markup


def phone_uz():
    style = [
        [number_uz],
    ]
    markup = ReplyKeyboardMarkup(keyboard=style, resize_keyboard=True, one_time_keyboard=True)
    return markup


def phone_en():
    style = [
        [number_en],
    ]
    markup = ReplyKeyboardMarkup(keyboard=style, resize_keyboard=True, one_time_keyboard=True)
    return markup


def choice_lang():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(uzb_lang, en_lang)
    return markup


def main_menu_en():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(search, cell, my_profil_en, my_posts_en)
    return markup


def main_menu_uz():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(search_inl, cell_inl, my_profil_uz, my_posts_uz)
    return markup


def main_mane_2_uz():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(ishlatilgan, yangi, xomashyo, kadr)
    return markup


def main_mane_2_en():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(ishlatilgani, yangii, xomashyoi, kadri)
    return markup


def sub_category_uz():
    makup = InlineKeyboardMarkup(row_width=2)
    makup.add(agro, tekstil, metal, mebel, plastik)
    return makup


def sub_category_en():
    makup = InlineKeyboardMarkup(row_width=2)
    makup.add(agroi, tekstili, metali, mebeli, plastiki)
    return makup


def btn_for_admin():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(btn_add_ball, btn_new_post, btn_add_admin)
    return markup


def btn_yes_no():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(btn_yes, btn_no)
    return markup


def btn_for_delete_post():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(btn_delete)
    return markup
