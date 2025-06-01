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


def print_person(person: Person) -> str:
    if isinstance(person, Student):
        return f"Полное имя: {person.full_name()}, ID: {person.get_id()}"
    else:
        return f"Полное имя: {person.full_name()}, ID: {person.get_id()}, Курсы: {', '.join(person.courses)}"


list_student = [
    Student('Саша', 'Макеев', '123'),
    Student('Толик', 'Пупкин', '334')
]

list_teacher = [
    Teacher('Имя1', 'Фамилия', '42222', ["Физика", "Астрономия"]),
    Teacher('Имя2', 'Фамилия2', '1000', ["Математика", "Геометрия"])
]


print("Студенты:")
for person in list_student:
    print(print_person(person))

print("Учителя:")
for person in list_teacher:
    print(print_person(person))