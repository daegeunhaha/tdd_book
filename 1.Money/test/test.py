import unittest
from moneyFactory import MoneyFactory
from const.moneyKind import MoneyKind
from bank import Bank

class Test(unittest.TestCase):

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')

    @classmethod
    def setUpClass(cls):
        print('setupclass')

    @classmethod
    def tearDownClass(cls):
        print('teardownclass')

    def testMultiplication(self):
        five = MoneyFactory.createMoney(MoneyKind.DOLLAR, 5)
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.DOLLAR, 10) == five.times(2))
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.DOLLAR, 15) == five.times(3))

    def testEquality(self):
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.DOLLAR, 5) == MoneyFactory.createMoney(MoneyKind.DOLLAR, 5))
        self.assertFalse(MoneyFactory.createMoney(MoneyKind.DOLLAR, 5) == MoneyFactory.createMoney(MoneyKind.DOLLAR, 6))
        self.assertFalse(MoneyFactory.createMoney(MoneyKind.DOLLAR, 5) == MoneyFactory.createMoney(MoneyKind.FRANC, 5))

    def testFrancMultiplication(self):
        five = MoneyFactory.createMoney(MoneyKind.FRANC, 5)
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.FRANC, 10) == five.times(2))
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.FRANC, 15) == five.times(3))

    def testCurrency(self):
        self.assertEqual("USD", MoneyFactory.createMoney(MoneyKind.DOLLAR, 1).currency())
        self.assertEqual("CHF", MoneyFactory.createMoney(MoneyKind.FRANC, 1).currency())

    def testSimpleAddition(self):
        bank = Bank()
        sum = MoneyFactory.createMoney(MoneyKind.DOLLAR, 5).plus(MoneyFactory.createMoney(MoneyKind.DOLLAR, 5))
        reduced = bank.reduce(sum)
        self.assertEqual(MoneyFactory.createMoney(MoneyKind.DOLLAR, 10), sum)
