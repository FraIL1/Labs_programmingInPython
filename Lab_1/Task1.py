num_1, num_2, num_3 = int(input()), int(input()), int(input())
print(max(num_1, num_2, num_3))  # выводим максимальное число из 3
print(min(num_1, num_2, num_3))  # выводим минимальное число из 3

if num_1 == num_2 == num_3:
    print("Числа являются равными")
else:
    print("Числа не являются равными")