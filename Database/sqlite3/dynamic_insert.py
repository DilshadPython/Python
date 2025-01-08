import sqlite3
# do not named the file sqlite3.py

# first create to the database but we need to connect
connentc_db = sqlite3.connect('mydatabase.db')

con = connentc_db.cursor()

# VARCHAR is characters you can make maximise
# REAL is real number or float
# TEXT is a long string or characters

# create table


def create_table():
    con.execute('CREATE TABLE Car(Name VARCHAR, Model VARCHAR, Version REAL,\
				Description TEXT)')


def insert_data():
    con.execute(
        "INSERT INTO Car VALUES('Audi', 'A5', 2017, 'Brand new zero miles')")
    con.execute(
        "INSERT INTO Car VALUES('Audi', 'A3', 2015, 'Used 160 000 miles')")
    con.execute("INSERT INTO Car VALUES('Audi', 'A7', 2016, 'New 35 000 miles')")
    con.execute(
        "INSERT INTO Car VALUES('Audi', 'A2', 2005, 'Used 61 233 miles')")
    con.execute(
        "INSERT INTO Car VALUES('BMW', 'XZ', 2010, 'Brand new zero miles')")
    con.execute(
        "INSERT INTO Car VALUES('Porsche', 'P10', 2014, 'New been used 10 000 miles')")
    con.execute(
        "INSERT INTO Car VALUES('Mercedes', 'ML', 2017, 'Brand new 1000 miles')")
    con.execute(
        "INSERT INTO Car VALUES('Ford', 'F16', 2018, 'Newe test only 15 000 miles')")
    # we make sure to save the data into db
    connentc_db.commit()


def dynamic_insert_data():
    dynamic_name = str(input('Enter Car name: '))
    dynamic_model = str(input('Enter Car model: '))
    dynamic_version = int(input('Enter the year: '))
    dynamic_desc = str(input('Enter the description: '))

    # to insert dynamic data
    con.execute('INSERT INTO Car(Name, Model, Version, Description) VALUES (?, ?, ?, ?)',
                (dynamic_name, dynamic_model, dynamic_version, dynamic_desc))
    connentc_db.commit()


# to insert dynamic data we need the dynamic_insert_data function
dynamic_insert_data()

# when we run con.commit we need to stop connect_db.close() make a comment
# connentc_db.close()
