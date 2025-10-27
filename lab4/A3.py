# Ввод и проверка последовательности
while True:
    sequence = input("Введите последовательность пакетов (0 и 1): ")

    if len(sequence) < 5:
        print("Ошибка: длина должна быть не меньше 5!")
        continue

    if not all(char in '01' for char in sequence):
        print("Ошибка: используйте только 0 и 1!")
        continue

    break

# Расчеты
total = len(sequence)
lost = sequence.count('0')

# Поиск самой длинной последовательности нулей
max_zeros = 0
current = 0

for char in sequence:
    if char == '0':
        current += 1
        if current > max_zeros:
            max_zeros = current
    else:
        current = 0

# Оценка качества
percent = (lost / total) * 100

if percent <= 1:
    quality = "Отличное"
elif percent <= 5:
    quality = "Хорошее"
elif percent <= 10:
    quality = "Удовлетворительное"
elif percent <= 20:
    quality = "Плохое"
else:
    quality = "Критическое"

# Вывод
print(f"\nПакетов: {total}, Потерь: {lost}")
print(f"Макс. последовательность потерь: {max_zeros}")
print(f"Потери: {percent:.1f}% - {quality} качество")