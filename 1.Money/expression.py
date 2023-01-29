from abc import ABC, abstractclassmethod

class Expression(ABC):

    @abstractclassmethod
    def test(cls):
        pass
