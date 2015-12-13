import csv
import sqlite3
import os
import radar

class RandomEviction(object):
    def __init__(self, params):
        self.params = params
        with open(params["csv_file"]) as f:
            self.headers = csv.DictReader(f).fieldnames

    def generate(self):
        eviction = {}
        if not os.path.isfile("addresses.db"):
            raise FileNotFoundError("Did you generate the sqlite database yet?")
        connection = sqlite3.connect("addresses.db")
        c = connection.cursor()
        row = c.execute('SELECT * FROM address ORDER BY RANDOM() LIMIT 1').fetchone()
        for key, value in zip(self.headers, row) :
            eviction[key] = value
        connection.close()
        eviction["date"] = radar.random_date(
                start = self.params["start_date"],
                stop = self.params["end_date"]
                )
        return eviction
