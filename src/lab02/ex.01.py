def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    Возвращает кортеж (минимум, максимум) из списка чисел.

    Args:
        nums: Список чисел (int или float)

    Returns:
        Кортеж (min, max)

    Raises:
        ValueError: Если список пуст
    """
    if not nums:
        raise ValueError("Список не может быть пустым")

    return min(nums), max(nums)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    Возвращает отсортированный список уникальных значений.

    Args:
        nums: Список чисел (int или float)

    Returns:
        Отсортированный список уникальных значений
    """
    return sorted(set(nums))


def flatten(mat: list[list | tuple]) -> list:
    """
    "Расплющивает" список списков/кортежей в один список.

    Args:
        mat: Список, содержащий списки или кортежи

    Returns:
        Один список со всеми элементами

    Raises:
        TypeError: Если встретился элемент, не являющийся списком или кортежем
    """
    result = []
    for item in mat:
        if not isinstance(item, (list, tuple)):
            raise TypeError("Все элементы должны быть списками или кортежами")
        result.extend(item)
    return result

# Тест 1: нормальный случай
print("min_max([3, -1, 5, 5, 0]):", min_max([3, -1, 5, 5, 0]))

# Тест 2: обработка ValueError
try:
    print("min_max([]):", min_max([]))
except ValueError as e:
    print(f"min_max([]): ValueError - {e}")

# Тест 3: уникальные значения
print("unique_sorted([3, 1, 2, 1, 3]):", unique_sorted([3, 1, 2, 1, 3]))

# Тест 4: нормальное расплющивание
print("flatten([[1, 2], [3, 4]]):", flatten([[1, 2], [3, 4]]))

# Тест 5: обработка TypeError
try:
    print("flatten([1, [3, 4]]):", flatten([1, [3, 4]]))
except TypeError as e:
    print(f"flatten([1, [3, 4]]): TypeError - {e}")