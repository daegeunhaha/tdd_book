from bank import Bank
from const.currency import Currency
from expression import Expression, Money, Sum


def test_multiplication():
    bank = Bank()
    five = Money(5, Currency.USD)
    assert Money(10, Currency.USD) == five.times(2).reduce(bank, Currency.USD)
    assert Money(15, Currency.USD) == five.times(3).reduce(bank, Currency.USD)


def test_equality():
    assert Money(5, Currency.USD) == Money(5, Currency.USD)
    assert Money(5, Currency.USD) != Money(6, Currency.USD)
    assert Money(5, Currency.USD) != Money(5, Currency.CHF)


def test_franc_multiplication():
    bank = Bank()
    five = Money(5, Currency.CHF)
    assert Money(10, Currency.CHF) == five.times(2).reduce(bank, Currency.CHF)
    assert Money(15, Currency.CHF) == five.times(3).reduce(bank, Currency.CHF)


def test_currency():
    assert "USD" == Money(1, Currency.USD).currency()
    assert "CHF" == Money(1, Currency.CHF).currency()


def test_simple_addition():
    bank = Bank()
    result_sum: Expression = Money(5, Currency.USD).plus(Money(5, Currency.USD))
    reduced: Money = result_sum.reduce(bank, Currency.USD)
    assert Money(10, Currency.USD) == reduced


def test_reduce_sum():
    result_sum: Sum = Sum(Money(3, Currency.USD), Money(4, Currency.USD))
    bank: Bank = Bank()
    result: Money = result_sum.reduce(bank, Currency.USD)
    assert Money(7, Currency.USD) == result


def test_reduce_money():
    bank: Bank = Bank()
    money: Money = Money(1, Currency.USD)
    result: Money = money.reduce(bank, Currency.USD)
    assert Money(1, Currency.USD) == result


def test_reduce_money_different_currency():
    bank: Bank = Bank()
    bank.add_rate(Currency.CHF, Currency.USD, 2)
    money: Money = Money(2, Currency.CHF)
    result: Money = money.reduce(bank, Currency.USD)
    assert Money(1, Currency.USD) == result


def test_identity_rate():
    assert 1 == Bank().rate(Currency.USD, Currency.USD)


def test_mixed_addition():
    five_bucks: Expression = Money(5, Currency.USD)
    ten_francs: Expression = Money(10, Currency.CHF)
    bank: Bank = Bank()
    bank.add_rate(Currency.CHF, Currency.USD, 2)
    result: Money = five_bucks.plus(ten_francs).reduce(bank, Currency.USD)
    assert Money(10, Currency.USD) == result


def test_sum_plus_money():
    five_bucks: Expression = Money(5, Currency.USD)
    ten_francs: Expression = Money(10, Currency.CHF)
    bank: Bank = Bank()
    bank.add_rate(Currency.CHF, Currency.USD, 2)
    result_sum: Expression = Sum(five_bucks, ten_francs).plus(five_bucks)
    result: Money = result_sum.reduce(bank, Currency.USD)
    assert Money(15, Currency.USD) == result


def test_sum_times():
    five_bucks: Expression = Money(5, Currency.USD)
    ten_francs: Expression = Money(10, Currency.CHF)
    bank: Bank = Bank()
    bank.add_rate(Currency.CHF, Currency.USD, 2)
    mult: Expression = Sum(five_bucks, ten_francs).times(2)
    result: Money = mult.reduce(bank, Currency.USD)
    assert Money(20, Currency.USD) == result
