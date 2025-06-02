class AutoRegister(type):
    def __new__(cls, name, bases, dct):
        if not hasattr(new_class, 'registry'):
            new_class.registry = []
        else:
            new_class.registry.append(new_class)
        super().__new__(cls, name, bases, dct)


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


for cls in BaseModel.registry:
    print(cls.__name__)
