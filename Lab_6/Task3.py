import pandas as pd

stud = pd.read_csv('students.csv')

# проверяю пропуски
print("Количество пропусков в каждом столбце:")
print(stud.isnull().sum()) # isnull().sum() подсчитывает количество пропусков в каждом столбце

# заполняю пропуски в Score средним значением
mean_score = stud['Score'].mean()
stud['Score'] = stud['Score'].fillna(mean_score) # fillna заменяет пропуски указанным значением

# удаляю строки с пропусками в Group
stud = stud.dropna(subset=['Group'])

print("\nДанные после обработки пропусков:")
print(stud.info())