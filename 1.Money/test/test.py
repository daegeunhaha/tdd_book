import unittest
from moneyFactory import MoneyFactory
from const.moneyKind import MoneyKind
from money import Money

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
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.FRANC, 5) == MoneyFactory.createMoney(MoneyKind.FRANC, 5))
        self.assertFalse(MoneyFactory.createMoney(MoneyKind.FRANC, 5) == MoneyFactory.createMoney(MoneyKind.FRANC, 6))
        self.assertFalse(MoneyFactory.createMoney(MoneyKind.DOLLAR, 5) == MoneyFactory.createMoney(MoneyKind.FRANC, 5))

    def testFrancMultiplication(self):
        five = MoneyFactory.createMoney(MoneyKind.FRANC, 5)
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.FRANC, 10) == five.times(2))
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.FRANC, 15) == five.times(3))

    def testCurrency(self):
        self.assertEqual("USD", MoneyFactory.createMoney(MoneyKind.DOLLAR, 1).currency())
        self.assertEqual("CHF", MoneyFactory.createMoney(MoneyKind.FRANC, 1).currency())

    def testDifferentClassEquality(self):
        self.assertTrue(Money(10, "CHF") == MoneyFactory.createMoney(MoneyKind.FRANC, 10))