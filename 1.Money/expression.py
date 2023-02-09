import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from money import Money
    from const.currency import Currency
    from bank import Bank

class Expression(abc.ABC):

    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def reduce(self, bank: 'Bank', to: 'Currency') -> 'Money':
        pass

    def plus(self, addend: 'Expression') -> 'Expression':
        from sum import Sum
        return Sum(self, addend)

    @abc.abstractmethod
    def times(self, multiplier: int) -> 'Expression':
        pass
