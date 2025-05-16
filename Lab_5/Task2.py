import numpy as np
import matplotlib.pyplot as plt


# создаю массив из 1000 случайных чисел с нормальным распределением:
data = np.random.normal(size=1000)


# создаю окно для графика размером 10 на 6
plt.figure(figsize=(10, 6))

# гистограмма:
# массив + кол-во столбцов + цвет заливки + цвет границ + прозрачность
plt.hist(data, bins=20, color='blue', edgecolor='black', alpha=0.7)

plt.title('Гистограмма случайных данных')
plt.xlabel('Значения')  # название оси x
plt.ylabel('Частота')   # название оси y

# настраиваю сетку:
# только горизонтальные линии сетки + прозрачность линий
plt.grid(axis='y', alpha=0.5)

plt.show()