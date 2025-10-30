"""
Текстовые утилиты для обработки и анализа текста.
"""

import re
from collections import Counter


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст: приводит к нижнему регистру, заменяет ё на е, удаляет лишние пробелы.
    
    Args:
        text: Исходный текст
        casefold: Приводить к нижнему регистру
        yo2e: Заменять ё/Ё на е/Е
        
    Returns:
        Нормализованный текст
    """
    if not text:
        return ""
    
    result = text
    
    # Замена ё на е
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')
    
    # Приведение к нижнему регистру
    if casefold:
        result = result.casefold()
    
    # Замена управляющих символов на пробелы
    result = re.sub(r'[\t\r\n]', ' ', result)
    
    # Удаление лишних пробелов
    result = re.sub(r'\s+', ' ', result).strip()
    
    return result


def tokenize(text: str) -> list[str]:
    """
    Разбивает текст на слова-токены.
    
    Args:
        text: Нормализованный текст
        
    Returns:
        Список токенов (слов)
    """
    # Регулярное выражение для поиска слов (буквы/цифры/подчеркивание + дефисы внутри слов)
    pattern = r'\w+(?:-\w+)*'
    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Подсчитывает частоты слов в списке токенов.
    
    Args:
        tokens: Список токенов
        
    Returns:
        Словарь {слово: частота}
    """
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает топ-N самых частых слов.
    
    Args:
        freq: Словарь частот
        n: Количество слов для возврата
        
    Returns:
        Список кортежей (слово, частота), отсортированный по убыванию частоты
    """
    # Сортировка: по убыванию частоты, при равенстве - по алфавиту
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


# Тесты для проверки функций
if __name__ == "__main__":
    # Тесты normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"
    
    # Тесты tokenize
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    
    # Тесты count_freq + top_n
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    
    # Тест тай-брейка при равной частоте
    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]
    
    print("Все тесты пройдены!")