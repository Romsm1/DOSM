import requests


def bgpu_image() -> None:
    url = f"http://static-maps.yandex.ru/1.x/"
    params = {
        "apikey": "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13",
        "ll": "127.540927,50.256563",
        "spn": "0.004457,0.00219",
        "l": "map"
    }

    response = requests.get(url, params)

    if response.status_code == 200:
        with open("map.png", "wb") as p:
            p.write(response.content)
            print('Изображение успешно сохранено!')
    else:
        print(f"Ошибка запроса: {response.status_code}")


bgpu_image()
