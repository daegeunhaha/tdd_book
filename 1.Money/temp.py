from typing import Type, cast

class Parent:
    def __init__(self):
        print('hello')

class Child(Parent):
    def __init__(self):
        super().__init__()
        print('world')

    def test(self) -> Parent:
        return Child()
    
child = Child()
child2 : Child = cast(Child, child.test())