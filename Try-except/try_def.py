def main():
    num = get_number()
    print(f'You have entered a {num}.')

def get_number():
    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("That's not a number, you need to enter a number.")
        else:
            # break is break or stop you from the loop
            #  but return is return the value from the function and stop you from the loop
            return number



if __name__ == "__main__":
    get_number()