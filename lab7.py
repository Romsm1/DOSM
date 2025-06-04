import csv
from abc import ABC, abstractmethod
from typing import Any
import json


class DataProcessor(ABC):
    @abstractmethod
    def load_data(self, source: str) -> None:
        pass

    @abstractmethod
    def process_data(self) -> Any:
        pass

    @abstractmethod
    def save_data(self, destination: str) -> None:
        pass


class TXTProcessor(DataProcessor):
    def __init__(self):
        self.data = []

    def load_data(self, source: str) -> None:
        print(f"Загрузка данных из TXT-файла: {source}")
        with open(source, 'r', encoding='utf-8') as file:
            self.data = file.readlines()

    def process_data(self) -> Any:
        print(f'Обработка данных TXT-файла')
        return len(self.data)

    def save_data(self, destination: str) -> None:
        print(f'Сохранение результата в {destination}')
        with open(destination, 'w', encoding='utf-8') as file:
            file.write(f'Количество записей: {len(self.data)}')


class CSVProcessor(DataProcessor):
    def __init__(self):
        self.data = []

    def load_data(self, source: str) -> None:
        print(f"Загрузка данных из CSV-файла: {source}")
        with open(source, 'r', encoding='utf-8') as file:
            read = csv.reader(file)
            self.data = list(read)

    def process_data(self) -> Any:
        print('Обработка данных CSV-файла')
        return len(self.data)

    def save_data(self, destination: str) -> None:
        print(f'Сохранение результата в {destination}')
        with open(destination, 'w', encoding='utf-8') as file:
            write = csv.writer(file)
            write.writerow([f'Количество записей: {len(self.data)}'])  
            write.writerow([len(self.data)])


class JSONProcessor(DataProcessor):
    def __init__(self):
        self.data = []

    def load_data(self, source: str) -> None:
        print(f"Загрузка данных из JSON-файла: {source}")
        with open(source, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def process_data(self) -> Any:
        print('Обработка данных JSON-файла')
        if isinstance(self.data, list):
            return len(self.data)
        elif isinstance(self.data, dict):
            return len(self.data.keys())
        return 0

    def save_data(self, destination: str) -> None:
        print(f'Сохранение результата в {destination}')
        result = {'Количество записей': len(self.data)}  
        with open(destination, 'w', encoding='utf-8') as file:
            json.dump(result, file, ensure_ascii=False, indent=4)


csv_processor = CSVProcessor()
json_processor = JSONProcessor()

csv_processor.load_data("data.csv")
json_processor.load_data("data.json")

csv_record_count = csv_processor.process_data()
json_record_count = json_processor.process_data()

print(f'Количество записей в CSV: {csv_record_count}')
print(f'Количество записей в JSON: {json_record_count}')  

csv_processor.save_data('output_csv.csv')
json_processor.save_data('output_json.json')
