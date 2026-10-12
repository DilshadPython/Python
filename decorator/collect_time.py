import time

def collect_time(func):
    def wrapper():
        print('Start time:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        func()
        print('End time:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    return wrapper

@collect_time
def func():
    time.sleep(2)
    print('\nEnd time:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

func()