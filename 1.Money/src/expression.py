import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bank import Bank
    from const.currency import Currency


class Expression(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def reduce(self, bank: "Bank", currency: "Currency") -> "Money":
        pass

    def plus(self, addend: "Expression") -> "Expression":
        return Sum(self, addend)

    def times(self, multiplier: int) -> "Expression":
        return Multiply(self, multiplier)


class Multiply(Expression):
    def __init__(self, multiplicand: "Expression", multiplier: int):
        super().__init__()
        self.multiplicand = multiplicand
        self.multiplier = multiplier

    def reduce(self, bank: "Bank", currency: "Currency") -> "Money":
        amount: int = self.multiplicand.reduce(bank, currency).amount() * self.multiplier
        return Money(amount, currency)


class Sum(Expression):
    def __init__(self, augend: "Expression", addend: "Expression") -> None:
        super().__init__()
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: "Bank", currency: "Currency") -> "Money":
        amount: int = (
            self.augend.reduce(bank, currency).amount()
            + self.addend.reduce(bank, currency).amount()
        )
        return Money(amount, currency)


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
