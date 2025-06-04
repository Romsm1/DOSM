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

# Создание data.txt
with open('data.txt', 'w', encoding='utf-8') as txtfile:
    txtfile.write("Имя, Возраст, Город\n")  # Заголовки
    txtfile.write("Анна, 22, Москва\n")
    txtfile.write("Иван, 30, Санкт-Петербург\n")
    txtfile.write("Ольга, 27, Новосибирск\n")

print("Файлы data.csv, data.json и data.txt успешно созданы.")
