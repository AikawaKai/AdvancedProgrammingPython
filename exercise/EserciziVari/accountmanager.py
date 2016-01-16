class Account(object):

    def __init__(self, init_amount):
        self.amount = init_amount

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount

    def balance(self):
        return self.amount


class SafeAccount(Account):

    def __init__(self, init_amount):
        self._amount = init_amount

    def safeGet(self):
        return self._amount

    def safeSet(self, amount):
        assert amount > 0, "You've tried to withdraw too much money from your account"
        self._amount = amount

    amount = property(safeGet, safeSet, None, "Managed Attribute")


if __name__ == "__main__":
    a = SafeAccount(1000)
    print("The current balance {0}".format(a.balance()))
    print(a.amount)
    a.withdraw(100)
    print(a.amount)
    a.deposit(750)
    print("The current balance {0}".format(a.balance()))
    # a.withdraw(3000)
    print("The current balance {0}".format(a.balance()))
    a.amount = -1000
