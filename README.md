#Fake Evictions

Let's generate some fake evictions!

This is a little Python utility for doing so. It uses the master address
list for Boston, which you can download
[here](https://data.cityofboston.gov/City-Services/Master-Address-List/t85d-b449)
(grab the CSV).

##Usage

This was written with Python 3 in mind, it's not super likely to work
easily with Python 2.


First convert the CSV file to a sqlite3 db:

```
sudo pip install -r requirements.txt
csvsql --db sqlite:///addresses.db --insert --table addresses Master_Address_List.csv
```

then we can run the little Python script:

```
python generate_evictions.py
```

and answer the prompts! Hooray fake data!
