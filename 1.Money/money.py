from typing import TypeVar
from expression import Expression

T = TypeVar('T', bound='Money')

class Money():
    
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

    def plus(self, other: 'Money') -> Expression:
        # todo: change to sum
        return Money(self._amount + other._amount, self._currency)