from matplotlib import pyplot as plt

experiens = [
    'Data Science',
    'Java',
    'PHP',
    'Python Tutorials',
    'Django FW',
    'JavaScript',
    'Flask'
]
7481 
more_read = [45, 10, 30, 75, 85, 55, 69]

plt.bar(books, more_read, color = 'green')

plt.title('Book Library')

plt.xlabel('Books')
plt.ylabel('Status')
plt.show()