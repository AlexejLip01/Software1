seq=open('sequences.0.txt')
# Читаем исходный файл
with open('commands.0.txt', 'r') as com:
    content = com.read()

# Обрабатываем содержимое
result = []
i = 0
while i < len(content):
    # Если текущий символ - цифра, а следующий - буква
    if content[i].isdigit() and i + 1 < len(content) and content[i + 1].isalpha():
        # Преобразуем цифру в число и повторяем букву нужное количество раз
        count = int(content[i])
        letter = content[i + 1]
        result.append(letter * count)
        i += 2  # Пропускаем два символа (цифру и букву)
    else:
        # Если не комбинация "цифра+буква", просто добавляем символ как есть
        result.append(content[i])
        i += 1

output = ''.join(result)

# Выводим преобразованный файл
print("Преобразованный файл:")
print(output)
