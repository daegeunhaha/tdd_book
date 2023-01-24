from typing import TypeVar
from money import Money
from const.moneyKind import MoneyKind
from moneyFactory import MoneyFactory

T = TypeVar('T', bound='Franc')

class Franc(Money):

    def __init__(self: T, amount: int, currency: str):
        super().__init__(amount, currency)
