def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            print(ch, end='')
        print()

def draw_right_triangle(rows, ch):
    for i in range(rows):
        for j in range(i + 1):
            print(ch, end='')
        print()

def draw_frame(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end='')
            else:
                print(' ', end='')
        print()

# Запуск программы
n = int(input("Строки (n): "))
m = int(input("Столбцы (m): "))
ch = input("Символ: ") or '#'

print(f"\nПрямоугольник {n}x{m}:")
draw_rectangle(n, m, ch)

print(f"\nТреугольник:")
draw_right_triangle(n, ch)

print(f"\nРамка {n}x{m}:")
draw_frame(n, m, ch)