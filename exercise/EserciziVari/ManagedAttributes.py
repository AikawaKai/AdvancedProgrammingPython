class Amount:

    def __init__(self, initial_amount):
        self.amount = initial_amount

    def deposit(self, value):
        self.amount += value

    def withdraw(self, value):
        self.amount -= value

    def balance(self):
        return self.amount


class SafeAccountProperty(Amount):

    def __init__(self, initial_amount):
        self.safe_amount = initial_amount

    def my_get(self):
        return self.safe_amount

    def my_set(self, value):
        if value < 0:
            raise Exception("Valore non può essere negativo")
        else:
            self.safe_amount = value

    amount = property(my_get, my_set, None, "")


if __name__ == '__main__':
    sa = SafeAccountProperty(100)
    print(sa.balance())
    sa.deposit(100)
    print(sa.balance())
    sa.withdraw(300)
    print(sa.balance())
