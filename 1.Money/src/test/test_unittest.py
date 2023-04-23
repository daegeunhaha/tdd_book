import unittest

from bank import Bank
from const.currency import Currency
from expression import Expression, Money, Sum


class Test(unittest.TestCase):
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    def testMultiplication(self) -> None:
        bank = Bank()
        five = Money(5, Currency.USD)
        self.assertTrue(Money(10, Currency.USD) == five.times(2).reduce(bank, Currency.USD))
        self.assertTrue(Money(15, Currency.USD) == five.times(3).reduce(bank, Currency.USD))

    def testEquality(self) -> None:
        self.assertTrue(Money(5, Currency.USD) == Money(5, Currency.USD))
        self.assertFalse(Money(5, Currency.USD) == Money(6, Currency.USD))
        self.assertFalse(Money(5, Currency.USD) == Money(5, Currency.CHF))

    def testFrancMultiplication(self) -> None:
        bank = Bank()
        five = Money(5, Currency.CHF)
        self.assertTrue(Money(10, Currency.CHF) == five.times(2).reduce(bank, Currency.CHF))
        self.assertTrue(Money(15, Currency.CHF) == five.times(3).reduce(bank, Currency.CHF))

    def testCurrency(self) -> None:
        self.assertEqual("USD", Money(1, Currency.USD).currency())
        self.assertEqual("CHF", Money(1, Currency.CHF).currency())

    def testSimpleAddition(self) -> None:
        bank = Bank()
        sum: Expression = Money(5, Currency.USD).plus(Money(5, Currency.USD))
        reduced: Money = sum.reduce(bank, Currency.USD)
        self.assertEqual(Money(10, Currency.USD), reduced)

    def testReduceSum(self) -> None:
        sum: Sum = Sum(Money(3, Currency.USD), Money(4, Currency.USD))
        bank: Bank = Bank()
        result: Money = sum.reduce(bank, Currency.USD)
        self.assertEqual(Money(7, Currency.USD), result)

    def testReduceMoney(self) -> None:
        bank: Bank = Bank()
        money: Money = Money(1, Currency.USD)
        result: Money = money.reduce(bank, Currency.USD)
        self.assertEqual(Money(1, Currency.USD), result)

    def testReduceMoneyDifferentCurency(self) -> None:
        bank: Bank = Bank()
        bank.add_rate(Currency.CHF, Currency.USD, 2)
        money: Money = Money(2, Currency.CHF)
        result: Money = money.reduce(bank, Currency.USD)
        self.assertEqual(Money(1, Currency.USD), result)

    def testArrayEquals(self) -> None:
        self.assertEqual(["abc"], ["abc"])

    def testIdentityRate(self) -> None:
        self.assertEqual(1, Bank().rate(Currency.USD, Currency.USD))

    def testMixedAddition(self) -> None:
        fiveBucks: Expression = Money(5, Currency.USD)
        tenFrancs: Expression = Money(10, Currency.CHF)
        bank: Bank = Bank()
        bank.add_rate(Currency.CHF, Currency.USD, 2)
        result: Money = fiveBucks.plus(tenFrancs).reduce(bank, Currency.USD)
        self.assertEqual(Money(10, Currency.USD), result)

    def testSumPlusMoney(self) -> None:
        fiveBucks: Expression = Money(5, Currency.USD)
        tenFrancs: Expression = Money(10, Currency.CHF)
        bank: Bank = Bank()
        bank.add_rate(Currency.CHF, Currency.USD, 2)
        sum: Expression = Sum(fiveBucks, tenFrancs).plus(fiveBucks)
        result: Money = sum.reduce(bank, Currency.USD)
        self.assertEqual(Money(15, Currency.USD), result)

    def testSumTimes(self) -> None:
        fiveBucks: Expression = Money(5, Currency.USD)
        tenFrancs: Expression = Money(10, Currency.CHF)
        bank: Bank = Bank()
        bank.add_rate(Currency.CHF, Currency.USD, 2)
        mult: Expression = Sum(fiveBucks, tenFrancs).times(2)
        result: Money = mult.reduce(bank, Currency.USD)
        self.assertEqual(Money(20, Currency.USD), result)
