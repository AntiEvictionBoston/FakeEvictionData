import csv
import random
import sqlite3
import os
import subprocess

class RandomEviction(object):
    def __init__(self, params):
        self.params = params

    def generate(self):
        if not os.path.isfile("addresses.db")
            raise FileNotFoundError("Did you generate the sqlite database yet?")
        connection = sqlite3.connect("addresses.db")
        c = connection.cursor()

        row = c.execute('SELECT * FROM address ORDER BY RANDOM() LIMIT 1').fetchone()


        connection.close()
