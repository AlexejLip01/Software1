password = input()

errors = []

if len(password) != 8:
    errors.append("Длина пароля не равна 8")

if not any(c.isupper() for c in password):
    errors.append("В пароле отсутствуют заглавные буквы")

if not any(c.islower() for c in password):
    errors.append("В пароле отсутствуют строчные буквы")

if not any(c.isdigit() for c in password):
    errors.append("В пароле отсутствуют цифры")

if not any(c in "*-#" for c in password):
    errors.append("В пароле отсутствуют специальные символы")

if any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*-#" for c in password):
    errors.append("В пароле используются непредусмотренные символы")

if errors:
    for error in errors:
        print(error)
else:
    print("Надежный пароль")
