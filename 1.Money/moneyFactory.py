from const.moneyKind import MoneyKind
from typing import Type
from money import Money


class MoneyFactory():
    
    @classmethod
    def createMoney(cls, moneyKind: MoneyKind, amount: int) -> Type[Money]:
        if moneyKind == MoneyKind.DOLLAR:
            return Money(amount, "USD")
        elif moneyKind == MoneyKind.FRANC:
            return Money(amount, "CHF")
