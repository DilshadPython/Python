msg = ' I am Python.'
try:
    print('This is not runing because we have string msg, but we try to converted to int')
    istr = int(msg)
except:
	print('This is working because -1 it\'s ')
	istr = -1

print('Check first', istr)
