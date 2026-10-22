class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.is_active = True

    def deactivate(self):
        self.is_active = False


u = User("Влад", "v@mail.com")
print(u.is_active)   # True
u.deactivate()
print(u.is_active)   # False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount    # прибавить

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount    # вычесть

    def get_balance(self):
        return self.balance
a = Account(100)
b = Account(500)

a.withdraw(100)
b.deposit(100)

print(a.get_balance())   # ждём 50
print(b.get_balance())   # ждём 500