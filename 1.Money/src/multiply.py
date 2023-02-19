from typing import TYPE_CHECKING

from expression import Expression
from money import Money

if TYPE_CHECKING:
    from bank import Bank
    from const.currency import Currency


class Multiply(Expression):
    def __init__(self, multiplicand: "Expression", multiplier: int):
        super().__init__()
        self.multiplicand = multiplicand
        self.multiplier = multiplier

    def reduce(self, bank: "Bank", currency: "Currency") -> "Money":
        amount: int = (
            self.multiplicand.reduce(bank, currency).amount() * self.multiplier
        )
        return Money(amount, currency)
