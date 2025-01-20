from multiply_number import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("AssertionError, 2 square results not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("AssertionError, 3 square results not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("AssertionError, -2 square results not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("AssertionError, -3 square results not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("AssertionError, 0 square results not 0")


if __name__ == "__main__":
    main()