import numpy as np
import matplotlib.pyplot as plt

# 1 график
x = np.linspace(0, 10, 50)  # 50 точек от 0 до 10
y = x ** 2

# 2 график
x_random = np.random.rand(30) * 10  # 30 случайных x от 0 до 10
y_random = np.random.rand(30) * 50  # 30 случайных y от 0 до 50

# 3 график
categories = ['A', 'B', 'C']
values = [3, 7, 2]  # значения для каждой категории


# создаем фигуру с 3-мя подзаголовками (1 строка, 3 столбца)
fig, (head1, head2, head3) = plt.subplots(1, 3, figsize=(15, 5))


# построение 1 графика
head1.plot(x, y, color='blue', linewidth=2)
head1.set_title('График y = x²')  # заголовок
head1.set_xlabel('x')      # подпись оси x
head1.set_ylabel('y')      # подпись оси y
head1.grid(True)           # включение сетки


# построение 2 графика
head2.scatter(x_random, y_random, color='orange', marker='o')
head2.set_title('Случайные точки')  # заголовок
head2.set_xlabel('x')    # подпись оси x
head2.set_ylabel('y')    # подпись оси y
head2.grid(True)         # включение сетки


# построение 3 графика
head3.bar(categories, values, color=['blue', 'green', 'red'])
head3.set_title('Категории')      # заголовок
head3.set_xlabel('Категория')     # подпись оси x
head3.set_ylabel('Значение')      # подпись оси y


plt.tight_layout()  # автоматическая регулировка расстояний между графиками
plt.show()