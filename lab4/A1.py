import random
import time
while True:
    try:

        N=int(input("Введите количество примеров:"))

correct = 0
total_time = 0

for i in range(N):
    a = random.randint(2,9)
    b = random.randint(2,9)
    right_answer=a*b

    print(f"\n{i+1}.{a}*{b}=?")
    start_time = time.time()
    while True:
        try:
            answer = int(input("Ответ:"))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    time_taken = time.time()-start_time
    total_time += time_taken

    if answer == right_answer:
        print(f"Верно!({time_taken:.1f}сек)")
        correct += 1
    else:
        print(f"Нет!Правильно: {right_answer}({time_taken:.1f}сек)")
print(f"\nСтатистика:")
print(f"Общее время: {total_time:.1f}сек")
print(f"Среднее время: {total_time/N:.1f}сек")
print(f"Правильных ответов:{correct} из {N}")
print(f"Процент правильных: {correct/N*100:.1f}%")

