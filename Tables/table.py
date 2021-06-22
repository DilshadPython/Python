 # pip install prettytable

from prettytable import PrettyTable

# Specify the column Names while initializing the table

newTable = PrettyTable(['Language', 'Versions', 'years'])

newTable.add_row(['Python', 3.3, 2010])
newTable.add_row(['Python', 3.4, 2011])

print(newTable)