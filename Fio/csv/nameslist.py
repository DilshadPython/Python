# we write to csv file when this program run
import csv

fname = input("Enter first name: ")
lname = input("Enter last name: ")
country = input("Enter country Name: ")

with open('listname.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow([fname, lname, country])
