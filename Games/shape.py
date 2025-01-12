def main():
    print_column(7)
    print_row(7)


def print_column(height):
    for _ in range(height):
        print('|')

def print_row(width):
    print('-->' * width)

main()
