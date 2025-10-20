# Ввод данных
prev = int(input())
curr = int(input())

# Вычисляем объем использованного газа
if curr >= prev:
    gas = curr - prev
else:
    gas = 10000 - prev + curr

# Вычисляем сумму оплаты
if gas <= 300:
    bill = 21.0
elif gas <= 600:
    bill = 21 + (gas - 300) * 0.06
elif gas <= 800:
    bill = 21 + 18 + (gas - 600) * 0.04
else:
    bill = 21 + 18 + 8 + (gas - 800) * 0.025

# Средняя цена
avg_price = bill / gas

# Вывод результатов
print(f"Объем использованного газа: {gas} куб. м")
print(f"Сумма к оплате: ${bill:.2f}")
print(f"Средняя цена за кубометр: ${avg_price:.2f}")
