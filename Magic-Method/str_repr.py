import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = str(a)


print('Str(a): {}'.format(str(a)))
print('Str(b): {}'.format(str(b)))

print('***' * 10)

print('Repr(a): {}'.format(repr(a)))
print('Repr(b): {}'.format(repr(b)))
