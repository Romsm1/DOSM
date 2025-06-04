import requests


def get_postal_code(api_key: str, address: str) -> None:
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": api_key,
        "geocode": address,
        "format": "json"
    }

    response = requests.get(url, params)

    if response.status_code == 200:
        data = response.json()
        if data['response']['GeoObjectCollection']['featureMember']:
            geo_object = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
            if 'postal_code' in geo_object['metaDataProperty']['GeocoderMetaData']['Address']:
                postal_code = geo_object['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
                print(f"Почтовый индекс для адреса '{address}': {postal_code}")
            else:
                print(f"Почтовый индекс для адреса '{address}' не найден.")
        else:
            print("Адрес не найден.")
    else:
        print(f"Ошибка запроса: {response.status_code}")


api_key = '8013b162-6b42-4997-9691-77b7074026e0'

address = input("Введите адрес: ")

get_postal_code(api_key, address)



# ПРИМЕРЫ АДРЕСОВ
# Москва, Красная площадь, 1
# Санкт-Петербург, Невский проспект, 28
# Новосибирск, Красный проспект, 100
# Екатеринбург, ул. Малышева, 51
# Казань, ул. Баумана, 1
# Ростов-на-Дону, пр. Ворошиловский, 1
# Владивосток, ул. Светланская, 1
# Нижний Новгород, ул. Большая Покровская, 1
# Челябинск, ул. Труда, 1
# Тюмень, ул. Республики, 1