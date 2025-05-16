import numpy as np
import matplotlib.pyplot as plt

# загружаю данные из файла
data = np.genfromtxt('task_7dop.csv', delimiter=',')

# разделяю данные на два столбца
x = data[:, 0]  # первый столбец ось x
y = data[:, 1]  # второй столбец ось y

# создаю график
plt.figure(figsize=(8, 5))  # размер графика
plt.plot(x, y, 'blue')


plt.title('График зависимости столбцов из task_7dop.csv')
plt.xlabel('Первый столбец')
plt.ylabel('Второй столбец')

plt.show()