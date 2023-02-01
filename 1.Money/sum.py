from typing import TypeVar
from expression import Expression
from money import Money

class Sum(Expression):

    # TODO: circular import?
    def __init__(self, lhs: Money, rhs: Money):
        self.lhs = lhs
        self.rhs = rhs