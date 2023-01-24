from const.moneyKind import MoneyKind
from typing import Type
from money import Money


class MoneyFactory():
    
    @classmethod
    def createMoney(cls, moneyKind: MoneyKind, amount: int) -> Type[Money]:
        from dollar import Dollar
        from franc import Franc
        if moneyKind == MoneyKind.DOLLAR:
            return Dollar(amount, "USD")
        elif moneyKind == MoneyKind.FRANC:
            return Franc(amount, "CHF")