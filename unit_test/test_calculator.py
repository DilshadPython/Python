from calculator import square

def main():
    test_square()


def test_square():
    # if square(2) != 4:
    #     print("2 square is not equal to 4")
    # if square(6) != 36:
    #     print("6 square is not equal to 36")
    # OR
    try:
        assert square(5) == 25
    except AssertionError:
        print("The number is not square result, AssertionError")
    try:
        assert square(4) == 16
    except AssertionError:
        print('4 is not square of 16')
    try:
        assert square(-6) == 36
    except AssertionError:
        print('-6 is git not square of 36')
    try:
        assert square(0) == 0
    except AssertionError:
        print('0 is not square of 0')


if __name__ == "__main__":
    test_square()
