class Parent:
    def __init__(self):
        self.greeting = "Hi, I'm a parent object."
    def __str__(self):
        return "string representation:" + self.greeting
class ChildA(Parent):
    def __init__(self):
        super().__init__()
        self.greeting = "Hi, I'm a child object."
    def __str__(self):
        return "string representation:" + self.greeting

class ChildB(Parent):
    pass


if __name__ == '__main__' :
    parent = Parent()
    print(parent.__str__())

    childA = ChildA()
    print(childA.__str__())

    childB = ChildB()
    print(childB.__str__())
