from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from money import Money

class Expression(ABC):

    def __init__(self) -> None:
        super().__init__()
