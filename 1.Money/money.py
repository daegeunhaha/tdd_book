from typing import TypeVar, Type

T = TypeVar('T', bound='Money')

class Money:
    
    def __init__(self: T, amount: int):
        self._amount = amount

    def __eq__(self: Type[T], other: Type[T]) -> bool:
        return (type(self) == type(other)) & (self._amount == other._amount)
