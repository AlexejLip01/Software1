x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

if x1 == 0 or y1 == 0 or x2 == 0 or y2 == 0:
    print("Ошибка: все координаты должны быть не равны 0")
else:

    if x1 > 0 and y1 > 0:
        quarter1 = 1
    elif x1 < 0 and y1 > 0:
        quarter1 = 2
    elif x1 < 0 and y1 < 0:
        quarter1 = 3
    else:
        quarter1 = 4

    if x2 > 0 and y2 > 0:
        quarter2 = 1
    elif x2 < 0 and y2 > 0:
        quarter2 = 2
    elif x2 < 0 and y2 < 0:
        quarter2 = 3
    else:
        quarter2 = 4

    if quarter1 == quarter2:
        print(f"Yes, {quarter1}")
    else:
        print("No")

