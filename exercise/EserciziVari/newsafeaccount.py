from metaclassdecorateallthemethods import *


class Account(object, metaclass=decorateAll(Counter)):

    def __init__(self, initial_amount):
        self.amount = initial_amount

    def withdraw(self, towithdraw):
        self.amount -= towithdraw

    def deposit(self, todeposit):
        self.amount += todeposit

    def balance(self):
        return self.amount


class SafeAccount(Account):

    def __init__(self, initial_amount):
        self._amount = initial_amount

    def getAmount(self):
        return self._amount

    def setAmount(self, amount):
        assert amount > 0, "Non è permesso avere un importo negativo"
        self._amount = amount

    amount = property(getAmount, setAmount, None, "SafeAccount")

if __name__ == '__main__':

    acc = Account(100)
    acc.withdraw(150)
    print(acc.balance())
    accSafe = SafeAccount(100)
    print(acc.balance())
    accSafe.withdraw(50)
