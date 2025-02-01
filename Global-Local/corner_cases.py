# If we look at this program the method will read the local variable not the global
# even we have defined in all methods the global balance changed the deposit to 20
# but when calculated it will read the local balance which is 100 not in line 8
# we have changed the deposit to 200 in line 11 but read the top one
balance = 33

def main():
    global balance
    balance = 100
    print("Your current balance is: ", balance)
    deposit(200)
    print("Your deposit balance is: ", balance)
    overdraft(500)
    print("Your balance now: ", balance)

def deposit(amount):
    global balance
    balance = 20
    balance += amount

def overdraft(amount):
    global balance
    balance = 75
    balance -= amount


if __name__ == "__main__":
    main()
