import csv
import random
import sqlite3
import os

class RandomEviction(object):
    def __init__(self, params):
        self.params = params
        self.write_csv_to_sqlite()

    def write_csv_to_sqlite(self):
        if os.path.isfile("./addresses.db")
            return None
        conn = sqlite3.connect("./addresses.db")
        conn.text_factory = str
        cur = conn.cur()



    def generate(self):

