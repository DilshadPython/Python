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


tomas = BankAccount(1000, 500, 150)
print(tomas)

jeam = BankAccount(50, 200, 600)
print(jeam)

# conbine them together
debit_card = tomas.debit_card + jeam.debit_card
credit_card = tomas.credit_card + jeam.credit_card
save_account = tomas.save_account + jeam.save_account

total = BankAccount(debit_card, credit_card, save_account)
print('Total ', total)