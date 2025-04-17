
"""Я особо не понял что именно надо вывести и решил сделать два варианта написания кода"""
n = int(input('Какой вариант ответа хотите увидеть, 1 или 2? '))

# 1 вариант
if n == 1:
    numbers = list(range(1, 21))

    # фильтрую и оставляю только чётные числа
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    # увеличиваю каждое число на 10
    plus_ten = list(map(lambda x: x + 10, numbers))

    # сортирую по убыванию
    sorted_desc = sorted(numbers, reverse=True)

    print(even_numbers)
    print(plus_ten)
    print(sorted_desc)


# 2 вариант
if n == 2:
    numbers = list(range(1, 21))

    # фильтрую и оставляю только чётные числа
    numbers_chet = list(filter(lambda x: x % 2 == 0, numbers))

    # увеличиваю каждое число на 10
    numbers_plus_ten = list(map(lambda x: x + 10, numbers_chet))

    # сортирую по убыванию
    numbers_sort = sorted(numbers_plus_ten, reverse=True)

    print(numbers_sort)
