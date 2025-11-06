

def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Подсчитывает, сколько раз каждое слово встречается в списке.

    Args:
        tokens: Список слов для подсчета

    Returns:
        Словарь, где ключ - слово, значение - количество вхождений

    Examples:
        >>> count_freq(["яблоко", "банан", "яблоко"])
        {'яблоко': 2, 'банан': 1}

        >>> count_freq(["да", "нет", "да", "может быть"])
        {'да': 2, 'нет': 1, 'может быть': 1}
    """
    # Создаем пустой словарь для результатов
    frequency_dict = {}

    # Проходим по каждому слову в списке
    for word in tokens:
        if word not in frequency_dict:
            # Если слова еще нет - добавляем со счетчиком 1
            frequency_dict[word] = 1
        else:
            # Если слово уже есть - увеличиваем счетчик на 1
            frequency_dict[word] += 1

    return frequency_dict

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]: 
    """Возвращает n наиболее часто встречающихся 
    элементов из словаря частот.

    Args:
        freq: Словарь, где ключи - это элементы (например, слова), 
        а значения - их частота встречаемости

        n: количество самых частовстречающихся элементов, которые нужно вернуть.
        По умолчанию равно 5.

    Returns:
        list[tuple[str, int]]: Список из `n` кортежей, 
        каждый из которых содержит элемент
        (строку) и его частоту (целое число), 
        отсротированные в порядке убывания частоты.
    
    """
    # Преобразуем словарь в список кортежей
    items = list(freq.items())

    # Сортируем по убыванию частоты, при равенстве - по алфавиту.lambda - ключ для сортировки по частотеб 
    sorted_items = sorted(items,  key=lambda x: (-x[1], x[0]))

    # Возвращаем первые n элементов
    return sorted_items[:n]

print("=== Тесты списка/словаря №1===")
tokens = ["a","b","a","c","b","a"]
result_for_count=count_freq(tokens)
result_for_top=top_n(result_for_count, n=2)
print("Словарь частот:", result_for_count)
print("Топ-2 слов:", result_for_top)


print("=== Тесты списка/словаря №2===")
tokens = ["bb","aa","bb","aa","cc"]
result_for_count=count_freq(tokens)
result_for_top=top_n(result_for_count, n=2)
print("Словарь частот:", result_for_count)
print("Топ-2 слов:", result_for_top)