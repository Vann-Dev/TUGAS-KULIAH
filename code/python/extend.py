class BaseClass():
    def __init__(self):
        self.baseAttribute = "Base Attribute"

    def baseMethod(self):
        print("Base method")


class ExtendedClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.extendAttribute = "Extended Attribute"

    def extendedMethod(self):
        print(self.extendAttribute)
        print(self.baseAttribute)
        self.baseMethod()

extend = ExtendedClass()

extend.extendedMethod()
