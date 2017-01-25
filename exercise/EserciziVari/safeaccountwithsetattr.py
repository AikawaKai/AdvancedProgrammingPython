class DynamicAccountSeAttr():

    def __init__(self, init_amount):
        self._withdraws = 0
        self._deposits = init_amount

    def deposit(self, value):
        self._deposits += value

    def withdraw(self, value):
        self._withdraws += value

    def __getattr__(self, name):
        if name == 'balance':
            return self._deposits - self._withdraws

if __name__ == '__main__':
    da = DynamicAccountSeAttr(100)
    da.withdraw(120)
    da.deposit(200)
    da.withdraw(60)
    print(da.balance)
