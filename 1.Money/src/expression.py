import abc
from typing import TYPE_CHECKING

from multiply import Multiply
from sum import Sum

if TYPE_CHECKING:
    from bank import Bank
    from const.currency import Currency
    from money import Money


class Expression(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def reduce(self, bank: "Bank", currency: "Currency") -> "Money":
        pass

    def plus(self, addend: "Expression") -> "Expression":
        return Sum(self, addend)

    def times(self, multiplier: int) -> "Expression":
        return Multiply(self, multiplier)
