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
        evictions = []
        if not os.path.isfile("addresses.db"):
            raise FileNotFoundError("Did you generate the sqlite database yet?")
        connection = sqlite3.connect("addresses.db")
        c = connection.cursor()
        sql_to_execute = 'SELECT * FROM address ORDER BY RANDOM() LIMIT {}'.format(self.params["number_to_generate"])
        rows = c.execute(sql_to_execute).fetchall()
        connection.close()

        for row in rows:
            evictions.append({ key: val for key, val in zip(self.headers, row) })

        for eviction in evictions:
            eviction["date"] = str(radar.random_date(
                    start = self.params["start_date"],
                    stop = self.params["end_date"]
                    ))
        evictions.sort(key = lambda d: d["date"])

        return evictions
