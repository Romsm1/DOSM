import re

# Задание 1
def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z.]+\.[a-zA-Z]{2,6}$'
    return re.match(pattern, email) is not None

print("Задание 1")
print(is_valid_email("example@mail.com"))
print(is_valid_email("bad-email@@.com"))


# Задание 2
def extract_dates(text: str) -> list[str]:
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)

print("Задание 2")
text = "Встреча 12-04-2023 и потом 15/05/2024"
print(extract_dates(text))


# Задание 3
def mask_numbers(text: str) -> str:
    pattern = r'\b\d+(\.\d+)?\b'
    return re.sub(pattern, '<num>', text)

print("Задание 3")
text = "У него было 5 яблок и 3.14 пирога"
print(mask_numbers(text))


# Задание 4
def is_strong_password(password: str) -> bool:
    if not 8 <= len(password) <= 20:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@#$%^&+=.]', password):
        return False
    return True

print("Задание 4")
print(is_strong_password("Strong1@"))
print(is_strong_password("plohoy"))


# Задание 5
def extract_tags(html: str) -> list[str]:
    pattern = r'<\/?(\w+)'
    return re.findall(pattern, html)

print("Задание 5")
html = "<html><body><h1>Title</h1></body></html>"
print(extract_tags(html))


# Задание 6
def find_repeated_words(text: str) -> list[str]:
    pattern = r'\b(\w+)\s+\1\b'
    return list(set(match.group(1) for match in re.finditer(pattern, text, re.IGNORECASE)))

print("Задание 6")
text = "помидор б  помидор тест и и тест тест а тест тест"
print(find_repeated_words(text))


# Задание 7
def split_words(text: str) -> list[str]:
    return re.findall(r'\b\w+\b', text)

print("Задание 7")
text = "Hello world!, how are you?"
print(split_words(text))
