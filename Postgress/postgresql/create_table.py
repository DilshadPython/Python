import psycopg2
# from config import config


# first create to the database but we need to connect

connection = psycopg2.connect(user="dilmac",
                                password="myadmin",
                                host="127.0.0.1",
                                port="5432",
                                database="university")
cursor = connection.cursor()


# create table
def create_table():
    cursor.execute('CREATE TABLE Students(Name VARCHAR(120), Gender VARCHAR(10), \
                About TEXT)')

# to create the table need to call the function
create_table()

connection.close()
