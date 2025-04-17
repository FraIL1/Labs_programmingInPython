def add(a, b):  # сумма
    return a + b
def subtract(a, b):  # вычитание
    return a - b
def multiply(a, b):  # умножение
    return a * b
def divide(a, b):  # деление + деление на ноль
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a // b