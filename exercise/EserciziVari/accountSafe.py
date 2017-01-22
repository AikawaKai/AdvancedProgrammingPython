from accountNotSafe import Account

class AccountSafe(Account):

    def __init__(self, init_amount):
        self._amount = init_amount

    def safe_get(self):
        return self._amount

    def safe_set(self, value):
        if value < 0 :
            raise Exception("OPERAZIONE NON CONCESSA")
        else:
            self._amount = value

    amount = property(safe_get, safe_set, None, "prova")

if __name__ == '__main__':
    myA = AccountSafe(1000)
    print(myA.get_Amount())
    myA.withdraw(300)
    print(myA.get_Amount())
    myA.deposit(400)
    print(myA.get_Amount())
    myA.withdraw(1500)
    print(myA.get_Amount())
