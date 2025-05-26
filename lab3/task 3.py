def cache(func):
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            print(f"Результат для {args} взят из кэша.")
            return cache_dict[args]

        result = func(*args)
        cache_dict[args] = result
        print(f"Результат для {args} вычислен и сохранен в кэш.")
        return result

    return wrapper


@cache
def factorial(n):
    if n < 0:
        return "Факториал определяется только для целых чисел."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(0))
print(factorial(2))
print(factorial(10))
print(factorial(998))
