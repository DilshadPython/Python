from files import LogFile, DelimFile

log = LogFile('log.txt')
c = DelimFile('text.csv', ',')

log.write('\nSend this message as log')
log.write('\nThis is second msg to send to log')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])