from typing import TypeVar
from money import Money

T = TypeVar('T', bound='Dollar')

class Dollar(Money):

    def times(self: T, multiplier: int) -> T:
        return Dollar(self._amount * multiplier)