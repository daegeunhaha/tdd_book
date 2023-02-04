import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from money import Money
    from const.moneyKind import MoneyKind

class Expression(abc.ABC):

    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def reduce(self, to: 'MoneyKind') -> 'Money':
        pass