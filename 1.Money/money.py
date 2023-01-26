from typing import TypeVar
from abc import *

T = TypeVar('T', bound='Money')

class Money():
    
    def __init__(self: T, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self: T, other: T) -> bool:
        return (self._currency == other.currency()) & (self._amount == other._amount)

    def times(self: T, multiplier: int) -> T:
        return Money(self._amount * multiplier, self._currency)

    def currency(self: T) -> str:
        return self._currency

    def plus(self: T, other: T) -> T:
        return Money(self._amount + other._amount, self._currency)