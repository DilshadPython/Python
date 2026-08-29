def main():
    num = get_number(prompt)
    print(f'You have entered a {num}.')

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


if __name__ == "__main__":
    get_number(prompt='Enter a number: ')