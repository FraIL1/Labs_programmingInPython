
# использую with для автоматического закрытия файла
with open('server_logs.txt', 'r') as file:
    lines = file.readlines()


count_success = 0
total_bytes = 0
ips_unique = []

# обрабатываю каждую строку в логах
for line in lines:
    # удаляю лишние пробелы и разбиваем строку по пробелам
    parts = line.strip().split()

    # проверка содержит ли строка все необходимое
    if len(parts) < 7:
        continue

    date = parts[0][1:-1]   # дата (ГГГГ-ММ-ДД)
    time = parts[1][1:-1]  # время (ЧЧ:ММ:СС)
    ip = parts[2][1:-1]  # IP-адрес (XXX.XXX.XXX.XXX)
    status = parts[5][1:-1]  # статус ответа (XXX)
    byte_str = parts[6][1:-1]  # размер ответа (XXXX)

    # подсчитываю кол-во успешных запросов
    if status == '200':
        count_success += 1

    # считаю общий размер
    total_bytes += int(byte_str)

    # cобираю уникальные IP
    if ip not in ips_unique:
        ips_unique.append(ip)


# сортировка строк в обратном порядке
sorted_logs = sorted(lines, reverse=True)


with open('log_analysis.txt', 'w') as file:
    file.write('Анализ логов:\n\n')
    file.write(f'Успешных запросов: {count_success}\n')
    file.write(f'Общий объем: {total_bytes/(1024*1024):.1f} MB\n') # переводим байты в мегабайты
    file.write(f'Уникальных IP адресов: {len(ips_unique)}\n\n')

    for i, log in enumerate(sorted_logs[:10], 1):
        # Убираем лишние переносы строк и нумеруем
        print(f"{i}. {log.strip()}")