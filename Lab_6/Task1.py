import pandas as pd

stud = pd.read_csv('students.csv')

print("Первые 5 строк датасета:")
print(stud.head())

# инфа данных
print("\nИнформация о данных:")
print(stud.info())

# статистика
print("\nОписательная статистика:")
print(stud.describe())

# средний балл
average_score = stud['Score'].mean() # mean вычисляет среднее значение
print(f"\nСредний балл студентов: {average_score:.2f}")

# кол-во студентов в каждой группе
students_per_group = stud['Group'].value_counts() # value_counts считает количество уникальных значений
print("\nКоличество студентов в каждой группе:")
print(students_per_group)