from squares import square

def main():
    test_square()

def test_square():
    if square(5) != 5:
        print("Square failed, this is not square of 5")
    if square(6) != 6:
        print("Square failed, this is not square of 6")

if __name__ == "__main__":
    main()