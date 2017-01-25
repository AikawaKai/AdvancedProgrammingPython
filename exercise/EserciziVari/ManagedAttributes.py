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
            raise Exception("Valore non può essere negativo (Property): ", value)
        else:
            self.safe_amount = value

    amount = property(my_get, my_set, None, "")

class SafeDescriptor:

    def __get__(self, instance, owner):
        return instance.my_amount

    def __set__(self, instance, value):
        if value < 0:
            raise Exception("Valore non può essere negativo (Descriptor): ", value)
        else:
            instance.my_amount = value


class SafeAccountDescriptor(Amount):
    def __init__(self, initial_amount):
        self.my_amount = initial_amount

    amount = SafeDescriptor()

if __name__ == '__main__':
    # SafeAccount with property #

    sa = SafeAccountProperty(100)
    print(sa.balance())
    sa.deposit(100)
    print(sa.balance())
    #sa.withdraw(300)
    #print(sa.balance())

    # SafeAccount with Descriptor #

    sa = SafeAccountDescriptor(100)
    print(sa.balance())
    sa.deposit(400)
    print(sa.balance())
    sa.withdraw(900)
