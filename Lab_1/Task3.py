from math import factorial

n = int(input())
print(factorial(n))  # вывод факториала числа n

# вывод чисел в обратном порядке от n до 1
while n > 0:
    print(n, end=' ')
    n = n - 1
print()