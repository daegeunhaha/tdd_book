from expression import Expression
from typing import TypeVar
from money import Money

# inhertence class에 대해 TypeVar를 어떻게 처리해야 하나 잘 모르겠다. bound to Bank로 해야 하나? 그냥 해두면 알아서 되나?
# 그럼 내가 TypeVar 정할 때 미래에 해당 클래스를 상속할 지도 모르는 것을 고려해서 해야하나? 흠..
# https://stackoverflow.com/questions/47896283/how-to-have-inherited-type-hints-in-python
# 일단 self, cls에는 type hint를 넣지 말자;

class Bank():

    def __init__(self) -> None:
        pass
    
    def reduce(self, expression: Expression) -> Money:
        pass