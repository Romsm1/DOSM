import csv
import json

# Создание data.csv
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Имя', 'Возраст', 'Город'])  # Заголовки
    writer.writerow(['Анна', '22', 'Москва'])
    writer.writerow(['Иван', '30', 'Санкт-Петербург'])
    writer.writerow(['Ольга', '27', 'Новосибирск'])

# Создание data.json
json_data = [
    {"name": "Анна", "age": 22, "city": "Москва"},
    {"name": "Иван", "age": 30, "city": "Санкт-Петербург"},
    {"name": "Ольга", "age": 27, "city": "Новосибирск"}
]

with open('data.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(json_data, jsonfile, ensure_ascii=False, indent=4)

print("Файлы data.csv и data.json успешно созданы.")
