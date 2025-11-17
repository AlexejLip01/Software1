# Ввод текста
text = input("Введите текст: ")

# Разбиваем текст на предложения
sentences = []
current_sentence = ""

for char in text:
    current_sentence += char
    if char in '.!?':
        # Убираем лишние пробелы в предложении
        cleaned_sentence = ' '.join(current_sentence.split())
        sentences.append(cleaned_sentence)
        current_sentence = ""


# Выводим предложения в столбик
for sentence in sentences:
    print(sentence)