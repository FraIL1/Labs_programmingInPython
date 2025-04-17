f = open('text.txt')
text = f.read()
f.close()

# начинаю поиск даты вручную
dates = []
i = 0
while i < len(text) - 9:  # т.к. в "DD.MM.YYYY" 10 символов, поэтому проверка с запасом
    # проверяю формат даты
    if (text[i].isdigit() and text[i+1].isdigit() and    # проверяю, состоит ли строка только из цифр
        text[i+2] == '.' and
        text[i+3].isdigit() and text[i+4].isdigit() and
        text[i+5] == '.' and
        text[i+6].isdigit() and text[i+7].isdigit() and
        text[i+8].isdigit() and text[i+9].isdigit()):
        # если нашел дату, то добавляю ее
        dates.append(text[i:i+10])
    i += 1

# меняю формат дат
update_dates = []
for i in dates:
    day = i[:2]
    month = i[3:5]
    year = i[6:]
    update_dates.append(f"{year}-{month}-{day}")

# сохраняю в файл
f = open('dates.txt', 'w')
f.write('\n'.join(update_dates))
f.close()

print('Даты:')
# сортирую и вывожу
for i in sorted(update_dates):
    print(i)