from message import hi

# pytest test_message.py
def main():
    test_default()
    test_argument()

# function has to return value or something
def test_default():
    assert hi() == 'Welcome back to, Python'

def test_argument():
    assert hi('Flask') == 'Welcome back to, Flask'


if __name__ == '__main__':
    main()