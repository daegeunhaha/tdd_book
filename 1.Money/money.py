from typing import TypeVar, Type
from abc import *

T = TypeVar('T', bound='Money')

class Money():
    
    def __init__(self: Type[T], amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self: Type[T], other: Type[T]) -> bool:
        return (self.currency() == other.currency()) & (self._amount == other._amount)

    def times(self: Type[T], multiplier: int) -> Type[T]:
        return Money(self._amount * multiplier, self.currency())

    def currency(self: Type[T]) -> str:
        return self._currency
