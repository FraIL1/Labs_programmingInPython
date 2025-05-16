import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# создаю фигуру и оси для графика
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 2 * np.pi)  # устанавливаю пределы по оси x
ax.set_ylim(-1.1, 1.1)  # устанавливаю пределы по оси y
ax.grid(True)  # включаю сетку


ax.set_title('Построение графика sin(x) по точкам')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')

# создаю пустую линию, которую буду обновлять
line, = ax.plot([], [], 'r-', linewidth=2)  # Красная линия толщиной 2px

# создаю точечный график
dots = ax.scatter([], [], color='blue', s=30)  # синие точки размером 30


x = np.linspace(0, 2 * np.pi, 100)  # 100 точек от 0 до 2π
y = np.sin(x)  # вычисляю sin для каждой точки


def init():
    line.set_data([], [])  # очищаю линию
    dots.set_offsets(np.empty((0, 2)))  # очищаю точки
    return line, dots


def update(limit):
    # берем первые точки из массива x и y
    current_x = x[:limit]
    current_y = y[:limit]

    # обновляю данные линии
    line.set_data(current_x, current_y)

    # обновляю точки
    dots.set_offsets(np.column_stack((current_x, current_y)))

    return line, dots


# создаем анимацию:
# количество кадров равное количеству точек + отрисовка + задержка между кадрами в миллисекундах
animation = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True, interval=50)

plt.tight_layout()  # автоматически подгоняю расположение элементов
plt.show()