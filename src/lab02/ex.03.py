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

print("\n=== Tuples Tests ===")
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))  # "Иванов И.И., гр. BIVT-25, GPA 4.60"
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))  # "Петров П., гр. IKBO-12, GPA 5.00"