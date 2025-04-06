n = int(input())

sum_all_num = 0

# берем число от 1 до n b выводим каждое и также выводим его квадрат
for i in range(1, n):
    sum_all_num += i
    print(i)
    print(i**2)

print(sum_all_num) # вывод суммы чисел от 1 до n