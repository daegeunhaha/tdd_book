from typing import TypeVar

T = TypeVar('T', bound='Dollar')

class Dollar:

    def __init__(self: T, amount: int):
        self.amount = amount

    def times(self: T, multiplier: int) -> T:
        return Dollar(self.amount * multiplier)