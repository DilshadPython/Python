import psycopg2

try:
    connection = psycopg2.connect(
        database='postgres',
        user='dilmac',
        password='~Azad#1973@ShvaN',
        host='127.0.0.1',
        port='5432'
    )

    connection.autocommit = True
except (Exception, psycopg2.Error) as error:
    if(connection):
        print("Failed to insert record into mobile table", error)

cursor = connection.cursor()
