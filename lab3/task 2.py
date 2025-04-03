from functools import lru_cache


@lru_cache(maxsize=None)  # кэш не ограничен по размеру
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)
    else:
        return "Факториал определяется только для целых чисел."


print(factorial(1))
print(factorial(7))
print(factorial(0))
print(factorial(2))
print(factorial(4))
