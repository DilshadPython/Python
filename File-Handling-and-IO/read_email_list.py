#!/usr/bin/python

readEmail = open('emailList.txt', 'r+')

str = readEmail.read(10)

print('The email list: ', str)
print('all in lowercase: ', str.lower())

readEmail.close()
