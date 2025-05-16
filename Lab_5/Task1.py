import numpy as np
import matplotlib.pyplot as plt


# создаем массив из 100 точек от 0 до 10
x = np.linspace(0, 10, 100)  # np.linspace создает линейное пространство

# вычисляю y и z
y = np.sin(x)
z = np.cos(x)

# строю графики
plt.figure(figsize=(10, 6))  # создаю окно для графика
plt.plot(x, y, label='sin(x)', color='blue')  # график sin
plt.plot(x, z, label='cos(x)', color='red')   # график cos


plt.title('Графики функций sin(x) и cos(x)')

# подписываю оси
plt.xlabel('x')  # название оси абсцисс
plt.ylabel('y, z')  # название оси ординат
plt.legend()
plt.grid(True)  # включаю отображение сетки

plt.show()
