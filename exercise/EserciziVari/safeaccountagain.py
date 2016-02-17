class Account(object):

    def __init__(self, initial_amount):
        self.amount = initial_amount

    def deposit(self, value):
        self.amount += value

    def withdraw(self, value):
        self.amount -= value

    def balance(self):
        return self.amount


class SafeAccount(Account):

    def __init__(self, initial_amount):
        self._amount = initial_amount

    def getAmount(self):
        return self._amount

    def setAmount(self, amount):
        assert amount >= 0, "Errore l'ammontare non può essere negativo"
        self._amount = amount
    amount = property(getAmount, setAmount)

if __name__ == '__main__':

    account = Account(100)
    account.deposit(50)
    print(account.balance())
    account.withdraw(160)
    print(account.balance())
    saccount = SafeAccount(100)
    saccount.deposit(50)
    print(saccount.balance())
    saccount.withdraw(160)
    print(saccount.balance())
