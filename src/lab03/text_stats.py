#!/usr/bin/env python3
"""
text_stats.py - скрипт для анализа текстовой статистики
ЛР3 — Тексты и частоты слов
Студент: Хужамова Тасмина Музаффаровна
Группа: БИВТ-25-4
"""

import sys
import os

# Добавляем путь для импорта наших модулей
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

# Импортируем наши функции из библиотеки
from text import normalize, tokenize, count_freq, top_n


def text_stats(text: str, table_mode: bool = False) -> None:
    """
    Анализирует текст и выводит статистику по словам.
    
    Args:
        text: Исходный текст для анализа
        table_mode: Если True, выводит результаты в виде таблицы
    """
    # 1. Нормализуем текст (приводим к нижнему регистру, убираем лишние пробелы)
    norm_text = normalize(text)
    
    # 2. Разбиваем на отдельные слова (токены)
    tokens = tokenize(norm_text)
    
    # 3. Подсчитываем частоту каждого слова
    freq = count_freq(tokens)
    
    # 4. Получаем статистику
    total_words = len(tokens)
    unique_words = len(freq)
    top_words = top_n(freq, n=5)
    
    # 5. Выводим результаты
    print(f'Всего слов: {total_words}')
    print(f'Уникальных слов: {unique_words}')
    print('Топ-5:')
    
    if table_mode:
        print_table_output(top_words)
    else:
        print_simple_output(top_words)


def print_simple_output(top_words):
    """
    Простой вывод топ-слов в формате 'слово:частота'
    
    Args:
        top_words: Список кортежей (слово, частота)
    """
    for word, count in top_words:
        print(f'{word}:{count}')


def print_table_output(top_words):
    """
    Красиво выровненный табличный вывод
    
    Args:
        top_words: Список кортежей (слово, частота)
    """
    if not top_words:
        print("Нет данных для отображения")
        return
    
    # Находим максимальную длину слова для красивого выравнивания
    max_word_len = max(len(word) for word, _ in top_words)
    
    # Заголовок таблицы
    header = "слово".ljust(max_word_len) + " | частота"
    separator = "-" * len(header)
    
    print(header)
    print(separator)
    
    # Выводим данные таблицы
    for word, count in top_words:
        print(f"{word.ljust(max_word_len)} | {count}")


def get_input_text():
    """
    Получает текст от пользователя разными способами
    
    Returns:
        Введенный текст
    """
    # Проверяем, есть ли аргументы командной строки
    if len(sys.argv) > 1:
        # Читаем из файла: python text_stats.py filename.txt
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Ошибка: файл {sys.argv[1]} не найден")
            return None
    else:
        # Интерактивный ввод
        print("Введите текст для анализа (можно несколько строк):")
        print("Для завершения ввода нажмите Ctrl+D (Linux/Mac) или Ctrl+Z (Windows):")
        
        try:
            return sys.stdin.read().strip()
        except EOFError:
            print("\nВвод завершен.")
            return None


def main():
    """
    Основная функция - получает текст и запускает анализ
    """
    # Проверяем, включен ли табличный режим
    table_mode = '--table' in sys.argv or os.getenv('TEXT_STATS_TABLE', '0') == '1'
    
    # Получаем текст
    text = get_input_text()
    
    if not text:
        print("Ошибка: текст не может быть пустым")
        return
    
    # Запускаем анализ
    text_stats(text, table_mode)


if __name__ == '__main__':
    main()