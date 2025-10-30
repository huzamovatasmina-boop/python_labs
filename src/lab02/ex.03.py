def format_record(rec: tuple[str, str, float]) -> str:
    """
    Форматирует запись студента в строку.

    Args:
        rec: Кортеж (ФИО, группа, GPA)

    Returns:
        Отформатированная строка вида "Фамилия И.О., гр. ГРУППА, GPA X.XX"

    Raises:
        ValueError: Если ФИО или группа пустые, или GPA отрицательный
        TypeError: Если неверные типы данных
    """
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("Запись должна быть кортежем из 3 элементов")

    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str) or not isinstance(gpa, (int, float)):
        raise TypeError("Неверные типы данных: ожидались (str, str, float)")

    # Обработка ФИО
    fio_clean = ' '.join(fio.split()).title()  # Убираем лишние пробелы и делаем заглавные буквы
    fio_parts = fio_clean.split()

    if len(fio_parts) < 2:
        raise ValueError("ФИО должно содержать минимум фамилию и имя")

    if not fio_clean or not group:
        raise ValueError("ФИО и группа не могут быть пустыми")

    if gpa < 0:
        raise ValueError("GPA не может быть отрицательным")

    # Формируем инициалы
    surname = fio_parts[0]
    initials = '.'.join(name[0].upper() for name in fio_parts[1:]) + '.'

    # Форматируем GPA с 2 знаками после запятой
    gpa_formatted = f"{gpa:.2f}"

    return f"{surname} {initials}, гр. {group}, GPA {gpa_formatted}"
'''
print("\n=== Tuples Tests ===")
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))  # "Иванов И.И., гр. BIVT-25, GPA 4.60"
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))  # "Петров П., гр. IKBO-12, GPA 5.00"
'''
print("\n=== Tuples Tests ===")

# Тест 1: нормальный случай с отчеством
try:
    result = format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))
    print(f"format_record(('Иванов Иван Иванович', 'BIVT-25', 4.6)): {result}")
except Exception as e:
    print(f"format_record(('Иванов Иван Иванович', 'BIVT-25', 4.6)): {type(e).__name__} - {e}")

# Тест 2: нормальный случай без отчества
try:
    result = format_record(("Петров Пётр", "IKBO-12", 5.0))
    print(f"format_record(('Петров Пётр', 'IKBO-12', 5.0)): {result}")
except Exception as e:
    print(f"format_record(('Петров Пётр', 'IKBO-12', 5.0)): {type(e).__name__} - {e}")

# Тест 3: нормальный случай с лишними пробелами
try:
    result = format_record(("    хужамова   тасмина   музаффаровна ", "ABB-01", 3.999))
    print(f"format_record(('  хужамова  тасмина  музаффаровна ', 'ABB-01', 3.999)): {result}")
except Exception as e:
    print(f"format_record(('  хужамова   тасмина   музаффаровна ', 'ABB-01', 3.999)): {type(e).__name__} - {e}")

# Тест 4: ошибка - пустое ФИО
try:
    result = format_record(("", "BIVT-25", 4.6))
    print(f"format_record(('', 'BIVT-25', 4.6)): {result}")
except Exception as e:
    print(f"format_record(('', 'BIVT-25', 4.6)): {type(e).__name__} - {e}")

# Тест 5: ошибка - пустая группа
try:
    result = format_record(("Иванов Иван", "", 4.6))
    print(f"format_record(('Иванов Иван', '', 4.6)): {result}")
except Exception as e:
    print(f"format_record(('Иванов Иван', '', 4.6)): {type(e).__name__} - {e}")

# Тест 6: ошибка - отрицательный GPA
try:
    result = format_record(("Иванов Иван", "BIVT-25", -1.0))
    print(f"format_record(('Иванов Иван', 'BIVT-25', -1.0)): {result}")
except Exception as e:
    print(f"format_record(('Иванов Иван', 'BIVT-25', -1.0)): {type(e).__name__} - {e}")

# Тест 7: ошибка - только фамилия
try:
    result = format_record(("Иванов", "BIVT-25", 4.6))
    print(f"format_record(('Иванов', 'BIVT-25', 4.6)): {result}")
except Exception as e:
    print(f"format_record(('Иванов', 'BIVT-25', 4.6)): {type(e).__name__} - {e}")


# Тест 8: ошибка - неверный тип GPA
try:
    result = format_record(("Иванов Иван", "BIVT-25", "4.6"))
    print(f"format_record(('Иванов Иван', 'BIVT-25', '4.6')): {result}")
except Exception as e:
    print(f"format_record(('Иванов Иван', 'BIVT-25', '4.6')): {type(e).__name__} - {e}")

# Тест 9: нормальный случай с округлением GPA
try:
    result = format_record(("Хужамова Тасмина", "IKBO-10", 3.456))
    print(f"format_record(('Хужамова Тасмина', 'IKBO-10', 3.456)): {result}")
except Exception as e:
    print(f"format_record(('Хужамова Тасмина', 'IKBO-10', 3.456)): {type(e).__name__} - {e}")