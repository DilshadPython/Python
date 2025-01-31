# we use + operator as overloading
# Before we define __str__ here run the file get this error
# py bank_account.py
# <__main__.BankAccount object at 0x7338e918e210>
class BankAccount:
    def __init__(self, debit_card=0, credit_card=0, save_account=0):
        self.debit_card = debit_card
        self.credit_card = credit_card
        self.save_account = save_account

    def __str__(self):
        return f"Debit account: {self.debit_card}, Credit account {self.credit_card}, Saving: {self.save_account}"

    def __add__(self, other):
        debit_card = self.debit_card + other.debit_card
        credit_card = self.credit_card + other.credit_card
        save_account = self.save_account + other.save_account
        return BankAccount(debit_card, credit_card, save_account)


tomas = BankAccount(1000, 500, 150)
print(tomas)

jeam = BankAccount(50, 200, 600)
print(jeam)

total = tomas + jeam
print('Total ', total)