import xlrd
import MySQLdb

'''
pip install xlrd
pip install mysqlclient
https://www.youtube.com/watch?v=YLXFEQLCogM
'''

test = xlrd.open_workbook('property-data.csv')
sheet = test.sheet_by_price('PRICE')
# sheet = text.shet_by_index(0)

# 
database = MySQLdb.connect(host='localhost', user='root', password='admin123', db='csvfile')

# get the cursor , which is used to traverse the database, line by line
cursor = database.cursor()

#create insert query
query = '''
		INSERT INTO csvtable (
							PROPERTY_REFERENCE,
							PRICE,
							BEDROOMS,
							BATHROOMS,
							HOUSE_NUMBER,
							ADDRESS,
							REGION,
							POSTCODE,
							PROPERTY_TYPE
						)
					VALUSE (%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

# create for loops to iterate through each row in the XLS file,
# starting at row 2 to skip the headers

for r in range(1, sheet.nrows):
	PROPERTY_REFERENCE = sheet.cell(r, 0).value
	PRICE = sheet.cell(r, 1).value
	BEDROOMS = sheet.cell(r, 2).value
	BATHROOMS = sheet.cell(r, 3).value
	HOUSE_NUMBER = sheet.cell(r, 4).value
	ADDRESS = sheet.cell(r, 5).value
	REGION = sheet.cell(r, 6).value
	POSTCODE = sheet.cell(r, 7).value
	PROPERTY_TYPE = sheet.cell(r, 8).value

# assign valuse from each rows
	values = (PROPERTY_REFERENCE,PRICE,BEDROOMS,BATHROOMS,HOUSE_NUMBER,ADDRESS,REGION,POSTCODE,PROPERTY_TYPE)

	# exceute sql query
	cursor.excute(query, values)

cursor.close()

database.commit()

database.close()

print('##########')
print('Alll done')
print('')

columns = str(sheet.ncols)
rows = str(sheet.nrows)
Print(' We have impored "%2B columns and %2B rows %2B " rows to MySQl')

