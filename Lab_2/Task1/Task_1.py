file = open('data.txt', 'r')
numbers = []

for line in file:
    num = line.strip()
    numbers.append(float(num))
file.close()

# нахожу сумму всех чисел
sum_num = 0
for num in numbers:
    sum_num += num

# нахожу среднее арифметическое
nums_avg = sum_num / len(numbers)

# нахожу максимальное число
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

# нахожу минимальное число
min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num


result = open('result.txt', 'w')

result.write(f"Сумма: {sum_num}\n")
result.write(f"Среднее: {nums_avg}\n")
result.write(f"Максимум: {max_num}\n")
result.write(f"Минимум: {min_num}\n")

result.close()
