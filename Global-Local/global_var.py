# when we create global var outside the method we will not be able to access but
# to access the global var which is balance here we have to use global word in each method
balance = 0

def main():
    global balance
    print("Your current balance is: ", balance)
    deposit(100)
    overdraft(500)
    print("Your balance now: ", balance)

def deposit(amount):
    global balance
    balance += amount

def overdraft(amount):
    global balance
    balance -= amount


if __name__ == "__main__":
    main()
