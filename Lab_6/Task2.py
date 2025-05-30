import pandas as pd

stud = pd.read_csv('students.csv')


high_score_students = stud[stud['Score'] > 80]
print("Студенты с баллом выше 80:")
print(high_score_students)

# сортирую по убыванию балла
sorted_students = high_score_students.sort_values('Score', ascending=False) #sort_values сортировка по указанному столбцу + сортировка по убыванию
print("\nСтуденты с баллом выше 80, отсортированные по убыванию:")
print(sorted_students)

# нахожу старшего и младшего студента
oldest_student = stud.loc[stud['Age'].idxmax()]# idxmax возвращают индекс строки с максимальным значением
youngest_student = stud.loc[stud['Age'].idxmin()] # idxmin возвращают индекс строки с минимальным значением
print("\nСамый старший студент:")
print(oldest_student)
print("\nСамый младший студент:")
print(youngest_student)