def isValidNumber(string):
    return string.isdigit() and len(string) in [13, 15, 16]


def getCheckSum(string):
    checkSum = 0
    # Обрабатываем цифры с шагом 2, начиная с предпоследней (алгоритм Луна)
    for i in range(len(string) - 2, -1, -2):
        digit = int(string[i]) * 2
        if digit > 9:
            checkSum += digit - 9
        else:
            checkSum += digit

    # Обрабатываем оставшиеся цифры
    for i in range(len(string) - 1, -1, -2):
        checkSum += int(string[i])

    return checkSum


def getCardType(string):
    if len(string) in [13, 16] and string.startswith("4"):
        return "Visa"
    if len(string) == 15 and (string.startswith("34") or string.startswith("37")):
        return "American Express"
    if len(string) == 16 and string[0] == '5' and string[1] in '12345':
        return "MasterCard"
    return "Invalid"


# Основная программа
cardNumber = input("Введите номер банковской карты: ").strip()

if isValidNumber(cardNumber):
    if getCheckSum(cardNumber) % 10 == 0:
        print(getCardType(cardNumber))
    else:
        print("Invalid")  # Не проходит проверку по алгоритму Луна
else:
    print("Invalid")  # Неправильная длина или не только цифры