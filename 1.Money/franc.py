from typing import TypeVar
from money import Money

T = TypeVar('T', bound='Franc')

class Franc(Money):

    def times(self: T, multiplier: int) -> T:
        return Franc(self._amount * multiplier)