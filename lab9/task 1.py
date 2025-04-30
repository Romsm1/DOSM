class InterfaceChecker(type):
    def __new__(cls, name, bases, dct):
        if 'load' not in dct or 'save' not in dct:
            method_missing = []
            if 'load' not in dct:
                method_missing.append('load')
            if 'save' not in dct:
                method_missing.append('save')
            raise TypeError(f'Класс {name} должен иметь следующие методы: {", ".join(method_missing)}')
        return super().__new__(cls, name, bases, dct)


class CorrectPlugin(metaclass=InterfaceChecker):
    def load(self):
        print('Загрузка данных')

    def save(self):
        print('Сохранение данных')


try:
    class BrokenPlugin(metaclass=InterfaceChecker):
        def load(self):
            print('Загрузка данных')
except TypeError as e:
    print(f'Ошибка: {e}')
