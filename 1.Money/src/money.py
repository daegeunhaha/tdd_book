from typing import TYPE_CHECKING

from const.currency import Currency
from expression import Expression

if TYPE_CHECKING:
    from bank import Bank
    from sum import Sum


class Money(Expression):
    def __init__(self, amount: int, currency: "Currency"):
        super().__init__()
        self._amount = amount
        self._currency = currency

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return (self._currency == other._currency) & (self._amount == other._amount)

    def currency(self) -> str:
        return self._currency.name

    def amount(self) -> int:
        return self._amount

    def reduce(self, bank: "Bank", currency: "Currency") -> "Money":
        rate: float = bank.rate(self._currency, currency)
        return Money(int(self._amount / rate), currency)
