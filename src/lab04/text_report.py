#!/usr/bin/env python3
"""
Скрипт для генерации отчетов по текстовой статистике.
ЛР4 — Файлы: TXT/CSV и отчёты
"""

import sys
from pathlib import Path

# Добавляем пути для импорта наших модулей
sys.path.append(str(Path(__file__).parent.parent))

from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv


def analyze_text(text: str):
    """
    Анализирует текст и возвращает статистику.
    
    Args:
        text: Текст для анализа
        
    Returns:
        Кортеж (общее_количество_слов, уникальные_слова, топ_слов)
    """
    # Используем функции из ЛР3
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)
    
    return len(tokens), len(freq), top_words


def generate_report(input_file: str, output_file: str, encoding: str = "utf-8"):
    """
    Генерирует отчет по одному файлу.
    
    Args:
        input_file: Путь к входному файлу
        output_file: Путь для сохранения CSV отчета
        encoding: Кодировка входного файла
    """
    try:
        # 1. Читаем файл
        text = read_text(input_file, encoding)
        
        # 2. Анализируем текст
        total_words, unique_words, top_words = analyze_text(text)
        
        # 3. Подготавливаем данные для CSV
        freq = count_freq(tokenize(normalize(text)))
        sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        
        csv_data = [(word, count) for word, count in sorted_words]
        
        # 4. Сохраняем CSV
        write_csv(csv_data, output_file, header=("word", "count"))
        
        # 5. Выводим статистику в консоль
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_words:
            print(f"{word}:{count}")
            
        print(f"\nОтчет сохранен в: {output_file}")
        
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: неправильная кодировка файла. Попробуйте --encoding cp1251")
        sys.exit(1)


def main():
    """
    Основная функция скрипта.
    """
    # Простая версия - хардкодим пути
    input_file = "data/lab04/input.txt"
    output_file = "data/lab04/report.csv"
    
    # Создаем папку data/lab04 если ее нет
    Path("data/lab04").mkdir(parents=True, exist_ok=True)
    
    print(f"Анализируем файл: {input_file}")
    generate_report(input_file, output_file)


if __name__ == "__main__":
    main()