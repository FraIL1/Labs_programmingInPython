import pandas as pd

stud = pd.read_csv('students.csv')

# группировка по группам
group_stats = stud.groupby('Group').agg({  # agg позволяет применить разные функции к разным столбцам
    'Score': 'mean',
    'Age': 'median'
}).rename(columns={
    'Score': 'Average Score',
    'Age': 'Median Age'
})
print("Статистика по группам:")
print(group_stats)

# Добавление столбца Passed
stud['Passed'] = stud['Score'].apply(lambda x: 1 if x >= 60 else 0) # apply применяет функцию к каждому элементу столбца
print("\nДанные с добавленным столбцом Passed:")
print(stud.head())