import sqlite3
# do not named the file sqlite3.py

# first create to the database but we need to connect
connentc_db = sqlite3.connect('mydatabase.db')

cor = connentc_db.cursor()

# VARCHAR is characters you can make maximise
# REAL is real number or float
# TEXT is a long string or characters

# create table


def create_table():
    cor.execute('CREATE TABLE Car(Name VARCHAR, Model VARCHAR, Version REAL,\
				Description TEXT)')


def insert_data():
    cor.execute(
        "INSERT INTO Car VALUES('Audi', 'A5', 2017, 'Brand new zero miles')")
    cor.execute(
        "INSERT INTO Car VALUES('Audi', 'A3', 2015, 'Used 160 000 miles')")
    cor.execute("INSERT INTO Car VALUES('Audi', 'A7', 2016, 'New 35 000 miles')")
    cor.execute(
        "INSERT INTO Car VALUES('Audi', 'A2', 2005, 'Used 61 233 miles')")
    cor.execute(
        "INSERT INTO Car VALUES('BMW', 'XZ', 2010, 'Brand new zero miles')")
    cor.execute(
        "INSERT INTO Car VALUES('Porsche', 'P10', 2014, 'New been used 10 000 miles')")
    cor.execute(
        "INSERT INTO Car VALUES('Mercedes', 'ML', 2017, 'Brand new 1000 miles')")
    cor.execute(
        "INSERT INTO Car VALUES('Ford', 'F16', 2018, 'Newe test only 15 000 miles')")
    # we make sure to save the data into db
    connentc_db.commit()


def dynamic_insert_data():
    dynamic_name = input('Enter Car name: ')
    dynamic_model = input('Enter Car model: ')
    dynamic_version = int(input('Enter the year: '))
    dynamic_desc = input('Enter the description: ')

    # to insert dynamic data
    cor.execute('INSERT INTO Car(Name, Model, Version, Description) VALUES (?, ?, ?, ?)',
                (dynamic_name, dynamic_model, dynamic_version, dynamic_desc))
    connentc_db.commit()


def read_from_enter():

    car_name = input(' Please enter the Car name: ')
    sql = "SELECT * FROM Car WHERE Name = ? "

    for row in cor.execute(sql, [(car_name)]):
        print(row)

read_from_enter()

connentc_db.close()
