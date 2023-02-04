from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from money import Money

class Expression(ABC):

    def __init__(self, operator: str, lhs: 'Money', rhs: 'Money') -> None:
        super().__init__()
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs