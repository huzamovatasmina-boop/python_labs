n = int(input("Число учасников: "))

count_online = 0
count_offline = 0

for _ in range(n):
    line = input("ФИО участников: ").strip()
    # Разбиваем строку и берем последний элемент как формат участия
    parts = line.split()
    if parts:  # Проверяем, что строка не пустая
        format_flag = parts[-1]
        if format_flag.lower() == "true":
            count_online += 1
        else:
            count_offline += 1

print(f"Онлайн: {count_online} " f"Офлайн: {count_offline}")
