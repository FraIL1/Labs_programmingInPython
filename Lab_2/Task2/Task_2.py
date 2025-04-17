num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')

# создаю функцию для проверки на числа
def number(s):
    return s.isdigit()  # этот метод позволяет проверить состоит ли строка только из цифр

# проверяю на числа
if not number(num1) or not number(num2):
    print("Ошибка: нужно вводить только числа!")
else:
    num1 = int(num1)
    num2 = int(num2)

    # проверяю деление на ноль
    if num2 == 0:
        print("Ошибка: на ноль делить нельзя!")
    else:
        result = num1 // num2
        print(result)
