from random import randint

# генерация списка из 20 случайных чисел от -100 до 100
list_random = []
for i in range(1, 21):
    list_random.append(randint(-100, 100))

# выбираем числа, которые делятся на 2 без остатка и добавляем их в новый список
nums_k2 = []
for num in list_random:
    if num % 2 == 0:
        nums_k2.append(num)

# выбираем числа, которые делятся на 3 без остатка и добавляем их в новый список
nums_k3 = []
for num in list_random:
    if num % 3 == 0:
        nums_k3.append(num)

print(nums_k2)
print(nums_k3)

# вычисляю среднее арифметическое
nums_avg = sum(list_random) / len(list_random)
print(nums_avg)