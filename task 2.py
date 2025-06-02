class AutoRegister(type):
    def __new__(cls, name, bases, dct):
        if not hasattr(cls, 'registry'):
            cls.registry = []
        if name != 'BaseModel':
            cls.registry.append(name)
        return super().__new__(cls, name, bases, dct)


class BaseModel(metaclass=AutoRegister):
    def __init__(self, name):
        self.name = name


class User(BaseModel):
    def __init__(self, name, number):
        super().__init__(name)
        self.number = number


class Product(BaseModel):
    def __init__(self, name, info, price):
        super().__init__(name)
        self.info = info
        self.price = price


for name in AutoRegister.registry:
    print(name)