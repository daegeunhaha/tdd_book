from expression import Expression
from typing import TypeVar

T = TypeVar('T', bound='Bank')

class Bank():

    def __init__(self: T) -> None:
        pass
    
    def reduce(self: T, expression: Expression) -> None:
        pass