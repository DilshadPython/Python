from message import hi


# pytest test_message.py

def main():
    test_default()
    test_argument()

# function has to return value or something
def test_default():
    assert hi() == 'Welcome back to, Python'

def test_argument():
    assert hi('Django') == 'Welcome back to, Django'
    for name in ['Java', 'Python', 'Javascript', 'DotNet']:
        assert hi(name) == f'Welcome back to, {name}'


if __name__ == '__main__':
    main()