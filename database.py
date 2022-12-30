import datetime
import sqlite3


class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_status(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE users SET status = ? WHERE user_id = ?", (status, user_id,))

    def select_user(self, id):
        with self.connection:
            return self.cursor.execute("select * from users where user_id = ?", (id,))

    def _users(self):
        with self.connection:
            return self.cursor.execute("select * from users").fetchall()

    def add_user(self, user_id, name, phone, lang):
        with self.connection:
            date = datetime.datetime.now()
            return self.cursor.execute(
                "INSERT INTO users ('user_id'  , 'username' , 'phone' , 'created_at' , 'lang') VALUES (?,?,?,?,?)",
                (user_id, name, phone, date.strftime("%Y-%m-%d"), lang))

    def search_posts(self, category_1, category_2):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM products where product_type = ? and sub_category = ?",
                                         (category_1, category_2,)).fetchall()
            return result

    def check_user_lang(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
            return result[7]

    def all_users(self, id):
        with self.connection:
            return self.cursor.execute("Select * from users where user_id = ?", (id,))

    def all_products(self):
        with self.connection:
            return self.cursor.execute("select * from products")

    def add_product(self, created_at, photo, user_id, user_name, product_type, sub_category, decription, sell_or_buy):
        with self.connection:
            return self.cursor.execute(
                """INSERT OR IGNORE INTO products(created_at, photo, user_id, user_name, product_type, sub_category, decription, sell_or_buy) VALUES (?,?,?,?,?,?,?,?)""",
                (created_at, photo, user_id, user_name, product_type, sub_category, decription, sell_or_buy))

    def coin(self, id):
        user_ball = self.cursor.execute("select ball from users where user_id = ?", (id,))
        for i in user_ball:
            ball = i[0]
            if i[0] >= 10:
                ball -= 10
                self.cursor.execute("update users set ball = ? where user_id = ?", (ball, id,))
                self.connection.commit()

                return True
            else:
                return False

    def my_posts(self, id):
        return self.cursor.execute("""SELECT * FROM products WHERE user_id = ?""", (id,))

    def get_phone(self, id):
        phone = self.cursor.execute("SELECT phone from users where user_id = ?", (id,))
        return phone

    def get_users(self):
        with self.connection:
            return self.cursor.execute("""select * from users""")
        # return users

    def set_ball(self, user_id, ball):
        with self.connection:
            return self.cursor.execute("UPDATE users SET ball = ? WHERE user_id = ?", (ball, user_id,))

    def new_posts(self, data):
        with self.connection:
            return self.cursor.execute("select * from products where created_at = ?", (data,))
