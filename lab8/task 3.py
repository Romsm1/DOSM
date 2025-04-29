from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Product(ABC):
    @abstractmethod
    def get_total_price(self) -> float:
        pass


@dataclass
class Item(Product):
    name: str
    price: float
    quantity: int

    def get_total_price(self) -> float:
        return self.price * self.quantity


@dataclass
class Order:
    items: list[Item] = field(default_factory=list)

    def total_sum(self) -> float:
        return sum(item.get_total_price() for item in self.items)

    def sorted_items_by_price(self) -> list[Item]:
        return sorted(self.items, key=lambda item: item.price, reverse=True)


item1 = Item(name='Мандарины', price=45.00, quantity=10)
item2 = Item(name='Пицца', price=1000.00, quantity=1)
item3 = Item(name='Вода', price=100.00, quantity=10)
item4 = Item(name='Шоколад', price=199.99, quantity=1)

order = Order()
order.items.extend([item1, item2, item3, item4])
print('Oтсортированный список товаров по убыванию цены: ')
for item in order.sorted_items_by_price():
    print(f'{item.name}: {item.price}')
