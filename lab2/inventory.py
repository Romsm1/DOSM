class Inventory:
    def __init__(self, capacity=80):
        if capacity > 80:
            raise ValueError("Максимальная вместимость инвентаря - 80кг.")
        self.__items = {}
        self.__weight_limit = capacity
        self.__current_weight = 0
       

    def __str__(self):
        return f'Инвентарь (вместимость: {self.__weight_limit}кг.), (содержимое: {self.__items})'

    def __iter__(self):
        return iter(self.__items.items())

    def __len__(self):
        return sum(self.__items.values())

    def __getitem__(self, key):
        return self.__items.get(key, 0)

    def __delitem__(self, key):
        if key in self.__items:
            self.__current_weight -= self.__items[key]
            del self.__items[key]

    def __setitem__(self, key, value):
        new_weight = self.__current_weight + value
        if new_weight > self.__weight_limit:
            raise ValueError("Превышена максимальная вместимость инвентаря!")
        self.__items[key] = value
        self.__current_weight = new_weight

    def __contains__(self, item):
        return item in self.__items

    def __add__(self, other):
        if not isinstance(other, Inventory):
            return NotImplemented
        new_capacity = max(self.__weight_limit, other.__weight_limit)
        if new_capacity > 80:
            raise ValueError("Объединенный инвентарь превышает макс. вместимость (80кг)!")
        new_inventory = Inventory(new_capacity)
        new_inventory.__items = self.__items.copy()
        for key, value in other:
            new_inventory.__items[key] = new_inventory.__items.get(key, 0) + value
        return new_inventory
