from const.moneyKind import MoneyKind
from money import Money

class MoneyFactory():
    
    @classmethod
    def createMoney(cls, moneyKind: MoneyKind, amount: int) -> 'Money':
        if moneyKind == MoneyKind.DOLLAR:
            return Money(amount, "USD")
        elif moneyKind == MoneyKind.FRANC:
            return Money(amount, "CHF")
        return Money(amount, "USD")
