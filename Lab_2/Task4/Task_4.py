f = open('text.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

# ищем email
emails = []
for word in text.split():  # разбиваю текст на отдельные слова и проверяю каждое слово
    if '@' in word and '.' in word:
        email = word.strip('.,!?')
        emails.append(email)

# сохраняем emails
f = open('emails.txt', 'w', encoding='utf-8')
for email in emails:
    f.write(email + '\n')
f.close()

# ищем номер телефона
phones = []
for i in range(len(text)-15):  # проверяю каждую позицию начала номера в тексте
    phone = text[i:i+16]
    if (phone.startswith('+7-') and  # проверяю, начинается ли строка с +7
        phone[3:6].isdigit() and phone[6] == '-' and  # проверяю, состоит ли строка только из цифр
        phone[7:10].isdigit() and phone[10] == '-' and
        phone[11:13].isdigit() and phone[13] == '-' and
        phone[14:16].isdigit()):
        phones.append(phone)

# сохраняем номер телефона
f = open('phones.txt', 'w', encoding='utf-8')
f.write('\n'.join(phones))
f.close()

# ищем слова с большой буквы
capital_words = []
for word in text.split():  # разбиваю текст на отдельные слова и проверяю каждое слово

    # проверяю, состоит ли строка из букв и начинается ли слово с заглавной буквы
    if word and word[0].isupper() and word[0].isalpha():
        clean_word = ''
        for i in word:
            if i.isalpha():
                clean_word += i
        if clean_word:
            capital_words.append(clean_word)

# сохраняем слова с большой буквы
f = open('capital_words.txt', 'w', encoding='utf-8')
f.write('\n'.join(capital_words))
f.close()
