import unittest
from const.currency import Currency
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
        five = Money(5, Currency.USD)
        self.assertTrue(Money(10, Currency.USD) == five.times(2))
        self.assertTrue(Money(15, Currency.USD) == five.times(3))

    def testEquality(self) -> None:
        self.assertTrue(Money(5, Currency.USD) == Money(5, Currency.USD))
        self.assertFalse(Money(5, Currency.USD) == Money(6, Currency.USD))
        self.assertFalse(Money(5, Currency.USD) == Money(5, Currency.CHF))

    def testFrancMultiplication(self) -> None:
        five = Money(5, Currency.CHF)
        self.assertTrue(Money(10, Currency.CHF) == five.times(2))
        self.assertTrue(Money(15, Currency.CHF) == five.times(3))

    def testCurrency(self) -> None:
        self.assertEqual("USD", Money(1, Currency.USD).currency())
        self.assertEqual("CHF", Money(1, Currency.CHF).currency())

    def testSimpleAddition(self) -> None:
        bank = Bank()
        sum : Expression = Money(5, Currency.USD).plus(Money(5, Currency.USD))
        reduced : Money = bank.reduce(sum, Currency.USD)
        self.assertEqual(Money(10, Currency.USD), reduced)

    def testPlusReturnsSum(self) -> None:
        five : Money = Money(5, Currency.USD)
        sum : Sum = five.plus(five)
        self.assertEqual(five, sum.augend)
        self.assertEqual(five, sum.addend)

    def testReduceSum(self) -> None:
        sum : Sum = Sum(Money(3, Currency.USD), Money(4, Currency.USD))
        bank : Bank = Bank()
        result : Money = bank.reduce(sum, Currency.USD)
        self.assertEqual(Money(7, Currency.USD), result)

    def testReduceMoney(self) -> None:
        bank : Bank = Bank()
        result : Money = bank.reduce(Money(1, Currency.USD), Currency.USD)
        self.assertEqual(Money(1, Currency.USD), result)

    def testReduceMoneyDifferentCurency(self) -> None:
        bank: Bank = Bank()
        bank.addRate(Currency.CHF, Currency.USD, 2)
        result: Money = bank.reduce(Money(2, Currency.CHF), Currency.USD)
        self.assertEqual(Money(1, Currency.USD), result)

    def testArrayEquals(self) -> None:
        self.assertEqual(['abc'], ['abc'])

    def testIdentityRate(self) -> None:
        self.assertEqual(1, Bank().rate(Currency.USD, Currency.USD))
