def main():
    num = get_number()
    print(f'You have entered a {num}.')

def get_number():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass


if __name__ == "__main__":
    get_number()