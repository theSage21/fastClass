class SomeClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def div(self):
        return self.x / self.y


class ChildClass(SomeClass):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self):
        return super().add() + self.z

    def sub(self):
        return super().sub() - self.z

    def div(self):
        return super().div() / self.z
