from matplotlib import pyplot as plt

books = ['Data Science', 'Biology', 'Chimiches', 'Python Tutorials', 'Django projects']

more_read = [12, 45, 73, 23, 42]

plt.bar(books, more_read, color = 'green')

plt.title('Book Library')

plt.xlabel('Books')
plt.ylabel('Status')
plt.show()