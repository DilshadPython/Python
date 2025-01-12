def main():
    display_square(10)


def display_square(square):
    for x in range(square):
        display_row(square)

def display_row(width):
    print('#' * width)


if __name__ == '__main__':
    main()
