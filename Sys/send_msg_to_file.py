import sys
import datetime

# create file named dill.dat 'a' use for append in other word adding msg 
sys.stdout = open('dill.dat', 'a')
current_date = datetime.date.today()
sys.stdout.write('This message send to dill.dat file now.\n')
# or you can use print instead of sys.stdout.write

print('This is the second msg I am sending to dill.dat but using print.\t', current_date, '\n')