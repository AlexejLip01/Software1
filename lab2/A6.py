h = int(input("Введите часы:"))

mm = int(input("Введите минуты:"))

ss = int(input("Введите секунды:"))

N = int(input("Введите количество пройденных секунд:"))

total_seconds = h * 3600 + mm * 60 + ss

future_total_seconds = (total_seconds + N) % 86400

future_hours = future_total_seconds // 3600
future_minutes = (future_total_seconds % 3600) // 60
future_seconds = future_total_seconds % 60

print(f"Через {N} секунд: {future_hours}:{future_minutes:02d}:{future_seconds:02d}")

