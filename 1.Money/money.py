from expression import Expression
from const.currency import Currency
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bank import Bank
    from sum import Sum

class Money(Expression):
    
    def __init__(self, amount: int, currency: 'Currency'):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return (self._currency == other._currency) & (self._amount == other._amount)

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency.name

    def plus(self, addend: 'Money') -> 'Sum':
        from sum import Sum
        return Sum(self, addend)

    def reduce(self, bank: 'Bank', to: 'Currency') -> 'Money':
        rate: float = bank.rate(self._currency, to)
        return Money(int(self._amount / rate), to)