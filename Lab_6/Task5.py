import matplotlib.pyplot as plt
import pandas as pd

stud = pd.read_csv('students.csv')

# Гистограмма распределения баллов
plt.figure(figsize=(10, 6))
plt.hist(stud['Score'], bins=20, edgecolor='black')
plt.title('Распределение баллов студентов')
plt.xlabel('Балл')
plt.ylabel('Количество студентов')
plt.grid(True)
plt.show()

# Столбчатая диаграмма среднего балла по группам
plt.figure(figsize=(10, 6))
stud.groupby('Group')['Score'].mean().plot(kind='bar', color='skyblue') # groupby группирует данные
plt.title('Средний балл по группам')
plt.xlabel('Группа')
plt.ylabel('Средний балл')
plt.xticks(rotation=0)
plt.grid(True)
plt.show()