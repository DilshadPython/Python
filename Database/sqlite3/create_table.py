import sqlite3
# do not named the file sqlite3.py

# first create to the database but we need to connect
connentc_db = sqlite3.connect('mydatabase.db')

con = connentc_db.cursor()

# create table
def create_table():
	con.execute('CREATE TABLE Car(Name VARCHAR, Model VARCHAR, Version REAL,\
				Description TEXT)')

# to create the table need to call the function
create_table()

connentc_db.close()