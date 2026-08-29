# we write to csv file when this program run
import csv

fname = input("Enter first name: ")
lname = input("Enter last name: ")
country = input("Enter country Name: ")

with open('dictnames.csv', 'a') as f:
    writer = csv.DictWriter(f, fieldnames=['fname', 'lname', 'country'])
    writer.writerow({'fname': fname, 'lname': lname, 'country': country})
