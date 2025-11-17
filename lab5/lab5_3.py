text = input("Введите текст: ")

# Разбиваем текст на слова
words = text.split()

# Формируем аббревиатуру из первых букв слов длиной >= 3
abbreviation = ''
for word in words:
    if len(word) >= 3:
        abbreviation += word[0].upper()

print("Аббревиатура:", abbreviation)