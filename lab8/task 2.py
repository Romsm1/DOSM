from abc import ABC, abstractmethod
from dataclasses import dataclass


class Person(ABC):
    @abstractmethod
    def full_name(self) -> str:
        pass

    @abstractmethod
    def get_id(self) -> str:
        pass


@dataclass
class Student(Person):
    first_name: str
    last_name: str
    student_id: str

    def full_name(self) -> str:
         return f"{self.first_name} {self.last_name}"


    def get_id(self) -> str:
        return self.student_id


@dataclass
class Teacher(Person):
    first_name: str
    last_name: str
    employee_id: str
    courses: list[str]

    def full_name(self) -> str:
         return f"{self.first_name} {self.last_name}"

    def get_id(self) -> str:
        return self.employee_id


def people_info(people: list[Person]):
    for person in people:
        print(f'Полное имя: {person.full_name()}, ID: {person.get_id()}')


students = [
    Student('Саша', 'Макеев', '123'),
    Student('Толик', 'Пупкин', '334')
]

teachers = [
    Teacher('Имя1', 'Фамилия', '42222', ["Физика", "Астрономия"]),
    Teacher('Имя2', 'Фамилия2', '1000', ["Математика", "Геометрия"])
]

people = students + teachers

people_info(people)
