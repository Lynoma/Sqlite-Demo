import sqlite3
import constants as cons
from Objects.Meal import Meal


class SqlHelper:

    # Initialise db onCreate
    def __init__(self):
        self.conn = sqlite3.connect(cons.PATH_TO_DB)
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS meals(sandwich TEXT, fruit TEXT, tablenb INT)')

    def add_item(self, object: Meal):
        self.c.execute('INSERT INTO meals VALUES (?,?,?)', (object.sandwich, object.fruit, object.tablenb))
        self.conn.commit()

    def add_items(self, objects: list[Meal]):
        for item in objects:
            self.c.execute('INSERT INTO meals VALUES (?,?,?)', (item.sandwich, item.fruit, item.tablenb))
        self.conn.commit()

    # Close db onDelete
    def __del__(self):
        self.conn.close()
