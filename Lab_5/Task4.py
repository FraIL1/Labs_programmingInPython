import numpy as np
import matplotlib.pyplot as plt

# генерирую матрицу 5 на 5 (от мин значение до макс значение)
matrix = np.random.randint(1, 11, size=(5, 5))


# создаю новое окно для графика размером 8x6 дюймов
plt.figure(figsize=(8, 6))


# данные для визуализации + цветовая схема + отключаю сглаживание для четких границ ячеек
heatmap = plt.imshow(matrix, cmap='viridis', interpolation='nearest')


# связь с тепловой картой + подпись цветовой шкалы
plt.colorbar(heatmap, label='Значение')

for i in range(matrix.shape[0]):  # количество строк
    for j in range(matrix.shape[1]):  # количество столбцов

        # добавляю текст в каждую ячейку и выравниваю по центру
        plt.text(j, i, matrix[i, j], ha='center', va='center', color='white', fontsize=12)


plt.title('Тепловая карта матрицы 5x5')

# убираю подписи осей
plt.xticks([])
plt.yticks([])

plt.show()