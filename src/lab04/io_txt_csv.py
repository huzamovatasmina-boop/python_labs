"""
Модуль для работы с текстовыми и CSV файлами.
ЛР4 — Файлы: TXT/CSV и отчёты
"""

import csv
from pathlib import Path
from typing import Union, Iterable, Sequence


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл и возвращает его содержимое как строку.

    Args:
        path: Путь к файлу (строка или Path объект)
        encoding: Кодировка файла (по умолчанию UTF-8)

    Returns:
        Содержимое файла как строка

    Raises:
        FileNotFoundError: Если файл не существует
        UnicodeDecodeError: Если неправильная кодировка

    Examples:
        >>> text = read_text("data/input.txt")
        >>> text = read_text("data/file.txt", encoding="cp1251")
    """
    # Преобразуем в Path объект для удобства
    file_path = Path(path)

    # Читаем файл с указанной кодировкой
    # Если файла нет - выбросится FileNotFoundError
    # Если кодировка неправильная - UnicodeDecodeError
    return file_path.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence], path: Union[str, Path], header: tuple[str, ...] = None
) -> None:
    """
    Записывает данные в CSV файл.

    Args:
        rows: Итерируемый объект со строками данных
        path: Путь для сохранения CSV файла
        header: Заголовок таблицы (опционально)

    Raises:
        ValueError: Если строки имеют разную длину

    Examples:
        >>> data = [("word", "count"), ("привет", 2)]
        >>> write_csv(data, "report.csv", header=("word", "count"))
    """
    file_path = Path(path)
    rows_list = list(rows)  # Преобразуем в список для проверки

    # Проверяем, что все строки одинаковой длины
    if rows_list:
        first_len = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_len:
                raise ValueError(
                    f"Строка {i} имеет длину {len(row)}, ожидалась {first_len}"
                )

    # Создаем родительские папки если их нет
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Записываем в CSV
    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        # Записываем заголовок если есть
        if header is not None:
            writer.writerow(header)

        # Записываем данные
        for row in rows_list:
            writer.writerow(row)


def ensure_parent_dir(path: Union[str, Path]) -> None:
    """
    Создает родительские директории если их нет.

    Args:
        path: Путь к файлу или директории

    Examples:
        >>> ensure_parent_dir("data/reports/final.csv")
        # Создаст папки data/ и data/reports/ если их нет
    """
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
