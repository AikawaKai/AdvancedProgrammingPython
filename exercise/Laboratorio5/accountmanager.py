class Account(object):

    def __init__(self, money):
        self.money = money

    def deposit(self, money):
        self.money += money

    def withdraw(self, moneyToWithdraw):
        assert (self.money - moneyToWithdraw) >= 0
        self.money -= moneyToWithdraw

    def balance(self):
        return self.money


class Account1(object):

    def __init__(self, money):
        self.money = money

    def deposit(self, money):
        self.money += money

    def withdraw(self, moneyToWithdraw):
        self.money -= moneyToWithdraw

    def balance(self):
        return self.money


class SafeAccount(Account1):

    def __init__(self, value):
        self._money = value

    def safeGetOnMoney(self):
        return self._money

    def safeSetOnMoney(self, value):
        assert value >= 0, "operation not permitted. Not enough money"
        self._money = value

    money = property(safeGetOnMoney, safeSetOnMoney, None, "property for non negative balance")
