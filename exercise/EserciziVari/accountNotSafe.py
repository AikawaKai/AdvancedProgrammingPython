class Account(object):

    def __init__(self, init_amount):
        self.amount = init_amount

    def get_Amount(self):
        return self.amount

    def withdraw(self,w_amount):
        self.amount -= w_amount

    def deposit(self, d_amount):
        self.amount += d_amount

if __name__ == '__main__':
    myA = Account(1000)
