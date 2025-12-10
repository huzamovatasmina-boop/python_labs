import re
from typing import Dict, List, Tuple


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализует текст: приводит регистр, заменяет ё на е, убирает лишние пробелы.

    Args:
        text: Исходный текст
        casefold: Приводить к нижнему регистру (по умолчанию True)
        yo2e: Заменять ё/Ё на е/Е (по умолчанию True)

    Returns:
        Нормализованный текст

    Examples:
        >>> normalize("ПрИвЕт\\nМИр\\t")
        'привет мир'
        >>> normalize("ёжик, Ёлка")
        'ежик, елка'
    """
    # Замена управляющих символов на пробелы
    text = re.sub(r"[\t\r\n\f\v]", " ", text)

    # Замена ё/Ё на е/Е
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    # Приведение к нижнему регистру
    if casefold:
        text = text.casefold()

    # Удаление лишних пробелов
    text = re.sub(r" +", " ", text)
    return text.strip()


def tokenize(text: str) -> List[str]:
    """
    Разбивает текст на слова (токены).

    Args:
        text: Текст для разбиения на слова

    Returns:
        Список найденных слов

    Examples:
        >>> tokenize("привет, мир!")
        ['привет', 'мир']
        >>> tokenize("по-настоящему круто")
        ['по-настоящему', 'круто']
    """
    # Убираем все не-словесные символы (кроме дефиса и пробелов)
    clear_text = re.sub(r"[^\w\s-]", " ", text)

    # Разбиваем на слова по пробелам
    new_text = clear_text.split()

    return new_text


def count_freq(tokens: List[str]) -> Dict[str, int]:
    """
    Подсчитывает, сколько раз каждое слово встречается в списке.

    Args:
        tokens: Список слов для подсчета

    Returns:
        Словарь, где ключ - слово, значение - количество вхождений

    Examples:
        >>> count_freq(["яблоко", "банан", "яблоко"])
        {'яблоко': 2, 'банан': 1}
    """
    frequency_dict = {}

    for word in tokens:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1

    return frequency_dict


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    """
    Возвращает n наиболее часто встречающихся элементов из словаря частот.

    Args:
        freq: Словарь частот
        n: Количество самых частовстречающихся элементов

    Returns:
        Список кортежей (слово, частота), отсортированные по убыванию частоты

    Examples:
        >>> top_n({'a': 3, 'b': 2, 'c': 1}, 2)
        [('a', 3), ('b', 2)]
    """
    # Преобразуем словарь в список кортежей
    items = list(freq.items())

    # Сортируем по убыванию частоты, при равенстве - по алфавиту
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))

    # Возвращаем первые n элементов
    return sorted_items[:n]


# Только тесты, которые запускаются при прямом запуске файла
if __name__ == "__main__":
    # Эти принты выполняются ТОЛЬКО когда запускаем: python text.py
    # При импорте: from text import normalize - этот код НЕ выполняется

    # Тесты для самопроверки
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]

    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
