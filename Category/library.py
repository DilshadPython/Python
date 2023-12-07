# Library Management System

import json


class Book:
	def __init__(self, title, author, year):
		self.title = title
		self.author = author
		self.year = year


class Library:
	def __init__(self, json_file):
		with open(json_file, 'r') as f:
			data = json.load(f)
		self.books = [Book(**book) for book in data['book']]

	def get_books_author(self, author):
		return [book for book in self.books if book.author == author]

# Question
# How could we modify the Library class to allow adding a new book?
'''
a. Add a method add_book(self, title, author, year) that a ppends a new 
   Book object to self.books.books

b. Modify the __init__ method to accept an additional Book object.books

c. Add a method add_book(self, book) that appends book to data['books']

d. It is not possible to add a new book to the Library
'''