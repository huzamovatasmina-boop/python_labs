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

print("=== Arrays Tests ===")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([]))
print(unique_sorted([3, 1, 2, 1, 3]))

print(flatten([[1, 2], [3, 4]]))
print(flatten([1, [3, 4]]))