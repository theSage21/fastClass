from collections import namedtuple

SC = namedtuple("SomeClass", "x y add sub div")
cc = namedtuple("ChildClass", "x y z add sub div")


def SomeClass(x, y):
    def add():
        return x + y

    def sub():
        return x - y

    def div():
        return x / y

    return SC(x, y, add, sub, div)


def ChildClass(x, y, z):
    sc = SomeClass(x, y)

    def add():
        return sc.add() + z

    def sub():
        return sc.sub() - z

    def div():
        return sc.div() / z

    return cc(x, y, z, add, sub, div)
