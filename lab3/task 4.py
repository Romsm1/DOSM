import time


def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f'Вызов функции {func.__name__} с аргументами: {args}, {kwargs}')
        try:
            result = func(*args, **kwargs)
            print(f'Функция {func.__name__} завершилась успешно. Результат: {result}')
            return result
        except Exception as e:
            print(f'Ошибка в функции {func.__name__}: {e}, Тип ошибки: {type(e).__name__}')
        finally:
            elapsed_time = time.time() - start_time
            print(f'Время выполнения {func.__name__}: {elapsed_time} секунд')

    return wrapper


@log
def divide(a, b):
    return a / b


divide(50, 2)
print()
divide(a=50, b=2)
print()
divide(42, 0) 