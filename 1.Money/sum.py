from expression import Expression
from typing import TYPE_CHECKING
from const.moneyKind import MoneyKind
from moneyFactory import MoneyFactory

if TYPE_CHECKING:
    from money import Money

class Sum(Expression):
    
    def __init__(self, augend: 'Money', addend: 'Money') -> None:
        super().__init__()
        self.augend = augend
        self.addend = addend

    def reduce(self, to: MoneyKind) -> 'Money':
        amount : int = self.augend._amount + self.addend._amount
        return MoneyFactory.createMoney(to, amount)