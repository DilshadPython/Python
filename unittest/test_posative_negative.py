# We using pytest for this test but first need to make sure is installed
# pytest test_posative_negative.py
from positive_negative import square

def main():
    test_positive()
    test_negative()
    test_zero()

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

if __name__ == "__main__":
    main()