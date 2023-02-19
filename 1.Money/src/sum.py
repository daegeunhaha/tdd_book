from typing import TYPE_CHECKING

from const.currency import Currency
from expression import Expression
from money import Money

if TYPE_CHECKING:
    from bank import Bank


class Sum(Expression):
    def __init__(self, augend: "Expression", addend: "Expression") -> None:
        super().__init__()
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: "Bank", currency: Currency) -> "Money":
        amount: int = (
            self.augend.reduce(bank, currency).amount()
            + self.addend.reduce(bank, currency).amount()
        )
        return Money(amount, currency)
