def main():
    print_square(3)

def print_square(n):
    # for each row in the square
    for i in range(n):
        # for each brick in row
        for j in range(n):
            print('#', end="")
        # here enter to the new line after 30 time * printed and back to first for loop 10 times
        print()

if __name__ == '__main__':
    main()