
from assign2 import WriteFile, CSVFormatter, LogFormatter

write_csv = WriteFile('test2.csv', CSVFormatter)
write_log = WriteFile('log2.txt', LogFormatter)

write_csv.write(['a', 'b,2', 'c', 'd'])
write_log.write('This is a log message')

write_csv.write(['1', '2', '3', '4'])
write_log.write('This is a second log message')


write_csv.close()
write_log.close()