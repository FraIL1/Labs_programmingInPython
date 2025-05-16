import numpy as np

# генерирую матрицу 5 на 5 (от мин значение до макс значение)
matrix = np.random.randint(1, 11, size=(5, 5))


# np.mean считает среднее арифметическое
mean_val = np.mean(matrix)


# np.max возвращает наибольшее значение
max_value = np.max(matrix)


# np.min возвращает наименьшее значение
min_value = np.min(matrix)


# np.sum с параметром axis=0 суммирует элементы столбцов по вертикали
column_sums = np.sum(matrix, axis=0)


print("Матрица:")
print(matrix)

# вывожу среднее значение с округлением до 2 знаков после запятой
print(f"\nСреднее значение: {mean_val:.2f}")

print(f"Максимальный элемент: {max_value}")
print(f"Минимальный элемент: {min_value}")
print("\nСумма по столбцам:")
print(column_sums)