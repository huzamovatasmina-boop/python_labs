"""
Модуль для конвертации между JSON и CSV форматами.
ЛР5 — JSON и конвертации
"""

import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Конвертирует JSON файл в CSV формат.

    Поддерживает JSON файлы содержащие список словарей.
    Например: [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]

    Args:
        json_path: Путь к исходному JSON файлу
        csv_path: Путь для сохранения CSV файла

    Raises:
        FileNotFoundError: Если JSON файл не существует
        ValueError: Если JSON пустой, не список или содержит не словари
    """
    # Преобразуем пути в Path объекты
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    # Проверяем существование JSON файла
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")

    # Читаем JSON файл
    with json_file.open("r", encoding="utf-8") as jf:
        try:
            data = json.load(jf)
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка чтения JSON: {e}")

    # Валидация данных
    if not data:
        raise ValueError("Пустой JSON файл")

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    # Создаем родительские папки если их нет
    csv_file.parent.mkdir(parents=True, exist_ok=True)

    # Получаем все уникальные ключи из всех словарей
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())

    # Сортируем ключи по алфавиту для единообразия
    fieldnames = sorted(all_keys)

    # Записываем CSV
    with csv_file.open("w", encoding="utf-8", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        writer.writeheader()

        for item in data:
            # Заполняем отсутствующие поля пустыми строками
            row = {key: item.get(key, "") for key in fieldnames}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Конвертирует CSV файл в JSON формат.

    Преобразует CSV в список словарей, где первая строка - заголовки.

    Args:
        csv_path: Путь к исходному CSV файлу
        json_path: Путь для сохранения JSON файла

    Raises:
        FileNotFoundError: Если CSV файл не существует
        ValueError: Если CSV файл пустой или не имеет заголовка
    """
    # Преобразуем пути в Path объекты
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    # Проверяем существование CSV файла
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

    # Читаем CSV файл
    with csv_file.open("r", encoding="utf-8") as cf:
        reader = csv.DictReader(cf)

        # Преобразуем в список
        data = list(reader)

    # Валидация данных
    if not data:
        raise ValueError("CSV файл пустой или не содержит данных")

    # Создаем родительские папки если их нет
    json_file.parent.mkdir(parents=True, exist_ok=True)

    # Записываем JSON
    with json_file.open("w", encoding="utf-8") as jf:
        json.dump(data, jf, ensure_ascii=False, indent=2)
