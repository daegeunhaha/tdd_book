from typing import TypeVar
from expression import Expression
from money import Money

T = TypeVar('T', bound='Sum')

class Sum(Expression):

    # self type?
    # circular import?
    # type checking? mypy?
    def __init__(self: T, lhs: Money, rhs: Money):
        pass