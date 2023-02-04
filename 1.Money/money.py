from expression import Expression
from sum import Sum
from const.moneyKind import MoneyKind

class Money(Expression):
    
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return (self._currency == other.currency()) & (self._amount == other._amount)

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency

    def plus(self, addend: 'Money') -> Sum:
        return Sum(self, addend)

    def reduce(self, to: MoneyKind) -> 'Money':
        return self