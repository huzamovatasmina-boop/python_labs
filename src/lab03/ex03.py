

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

tokens=["a","b","a","c","b","a"]
result=count_freq(tokens)
print(result)