class MyAccount:
    # the _balance here show as private
    def __init__(self):
        self._balance = 0

    # @property is a instance varable which allowed me to protcted
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        return self

    def withdraw(self, amount):
        self._balance -= amount
        return self

def main():
    account = MyAccount()
    print('My current balance:', account.balance)
    account.deposit(250)
    account.withdraw(100)
    print('My balance now is: ', account.balance)


if __name__ == '__main__':
    main()