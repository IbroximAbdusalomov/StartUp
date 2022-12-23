from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

number = KeyboardButton("Telefon raqamni jo‘natish", request_contact=True)
uzb_lang = InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data='uz')
en_lang = InlineKeyboardButton("🇺🇸 English", callback_data='en')

# uz
search_inl = InlineKeyboardButton("🔎 Qidirish", callback_data='search')
mypr_inl = InlineKeyboardButton("💼 Mening kabinetim", callback_data='mypr')
cell_inl = InlineKeyboardButton("🛍 Sotish", callback_data='cell')

# en
search = InlineKeyboardButton("🔎 Search", callback_data='search')
mypr = InlineKeyboardButton("💼 My profile", callback_data='mypr')
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

my_posts_uz = InlineKeyboardButton(text="Mening e'lonlarim", callback_data='mypost')
my_profil_uz = InlineKeyboardButton(text="Mening profilm", callback_data='myprofil')

my_posts_en = InlineKeyboardButton(text="My posts", callback_data='mypost')
my_profil_en = InlineKeyboardButton(text="My profile", callback_data='myprofil')


def mycb_uz():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(my_posts_uz, my_profil_uz)
    return markup


def mycb_en():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(my_posts_en, my_profil_en)
    return markup


def phone():
    style = [
        [number],
    ]
    markup = ReplyKeyboardMarkup(keyboard=style, resize_keyboard=True, one_time_keyboard=True)
    return markup


def choice_lang():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(uzb_lang, en_lang)
    return markup


def main_menu_en():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(search, mypr, cell)
    return markup


def main_menu_uz():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(search_inl, mypr_inl, cell_inl)
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
