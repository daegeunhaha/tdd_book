from expression import Expression
from typing import TYPE_CHECKING
from const.currency import Currency
from money import Money

if TYPE_CHECKING:
    from bank import Bank

class Sum(Expression):
    
    def __init__(self, augend: 'Expression', addend: 'Expression') -> None:
        super().__init__()
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: 'Bank', to: Currency) -> 'Money':
        amount : int = self.augend.reduce(bank, to).amount() + self.addend.reduce(bank, to).amount()
        return Money(amount, to)
