import unittest
from moneyFactory import MoneyFactory
from const.moneyKind import MoneyKind
from bank import Bank
from expression import Expression
from money import Money
from sum import Sum

class Test(unittest.TestCase):

    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    @classmethod
    def setUpClass(cls) -> None:
        print('setupclass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownclass')

    def testMultiplication(self) -> None:
        five = MoneyFactory.createMoney(MoneyKind.DOLLAR, 5)
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.DOLLAR, 10) == five.times(2))
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.DOLLAR, 15) == five.times(3))

    def testEquality(self) -> None:
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.DOLLAR, 5) == MoneyFactory.createMoney(MoneyKind.DOLLAR, 5))
        self.assertFalse(MoneyFactory.createMoney(MoneyKind.DOLLAR, 5) == MoneyFactory.createMoney(MoneyKind.DOLLAR, 6))
        self.assertFalse(MoneyFactory.createMoney(MoneyKind.DOLLAR, 5) == MoneyFactory.createMoney(MoneyKind.FRANC, 5))

    def testFrancMultiplication(self) -> None:
        five = MoneyFactory.createMoney(MoneyKind.FRANC, 5)
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.FRANC, 10) == five.times(2))
        self.assertTrue(MoneyFactory.createMoney(MoneyKind.FRANC, 15) == five.times(3))

    def testCurrency(self) -> None:
        self.assertEqual("USD", MoneyFactory.createMoney(MoneyKind.DOLLAR, 1).currency())
        self.assertEqual("CHF", MoneyFactory.createMoney(MoneyKind.FRANC, 1).currency())

    def testSimpleAddition(self) -> None:
        bank = Bank()
        sum : Expression = MoneyFactory.createMoney(MoneyKind.DOLLAR, 5).plus(MoneyFactory.createMoney(MoneyKind.DOLLAR, 5))
        reduced : Money = bank.reduce(sum, MoneyKind.DOLLAR)
        self.assertEqual(MoneyFactory.createMoney(MoneyKind.DOLLAR, 10), reduced)

    def testPlusReturnsSum(self) -> None:
        five : Money = MoneyFactory.createMoney(MoneyKind.DOLLAR, 5)
        sum : Sum = five.plus(five)
        self.assertEqual(five, sum.augend)
        self.assertEqual(five, sum.addend)

    def testReduceSum(self) -> None:
        sum : Sum = Sum(MoneyFactory.createMoney(MoneyKind.DOLLAR, 3), MoneyFactory.createMoney(MoneyKind.DOLLAR, 4))
        bank : Bank = Bank()
        result : Money = bank.reduce(sum, MoneyKind.DOLLAR)
        self.assertEqual(MoneyFactory.createMoney(MoneyKind.DOLLAR, 7), result)

    def testReduceMoney(self) -> None:
        bank : Bank = Bank()
        result : Money = bank.reduce(MoneyFactory.createMoney(MoneyKind.DOLLAR, 1), MoneyKind.DOLLAR)
        self.assertEqual(MoneyFactory.createMoney(MoneyKind.DOLLAR, 1), result)
