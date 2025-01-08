import sqlite3
# do not named the file sqlite3.py

# first create to the database but we need to connect
connentc_db = sqlite3.connect('mydatabase.sqlite')

# the coursore is tell the mouse where to go and what to do it will be the same for
# sqlite3 and myssql and postgresql

con = connentc_db.cursor()
'''
	when you run python3 sqlite3.py will automatically create sqlite3 file
 	for you in current directory.
 '''

connentc_db.close()
