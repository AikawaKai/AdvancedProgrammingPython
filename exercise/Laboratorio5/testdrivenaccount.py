from unittest import TestCase
from unittest import main
from accountmanager import *


class TestingAccount(TestCase):

    def testDeposit(self):
        account = Account(100)
        account.deposit(100)
        self.assertEqual(200, account.balance())
        account.deposit(100)
        self.assertEqual(300, account.balance())

    def testWithdraw(self):
        account = Account(100)
        account.deposit(100)
        account.withdraw(50)
        self.assertEqual(150, account.balance())
        account.withdraw(100)
        self.assertEqual(50, account.balance())

    def testNonNegativeBalance(self):
        account = Account(100)
        self.assertRaises(AssertionError, account.withdraw, 150)
        #  self.assertGreaterEqual(account.balance(), 0)


class TestingSafeAccount(TestCase):

    def testSafeAccount(self):
        account = SafeAccount(10)
        self.assertEqual(10, account.balance())
        account.deposit(50)
        self.assertEqual(60, account.balance())
        # self.assertRaises(AssertionError, SafeAccount, -10)
        self.assertRaises(AssertionError, account.withdraw, 70)

if __name__ == '__main__':
    main()
