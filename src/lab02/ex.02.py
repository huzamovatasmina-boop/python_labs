def _validate_rectangular(mat: list[list[float | int]]) -> None:
    """
    Проверяет, что матрица прямоугольная (все строки одинаковой длины).

    Args:
        mat: Матрица (список списков)

    Raises:
        ValueError: Если матрица рваная (строки разной длины)
    """
    if not mat:
        return []

    first_len = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != first_len:
            raise ValueError(f"Матрица рваная: строка {i} имеет длину {len(row)}, ожидалась {first_len}")


def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    """
    Транспонирует матрицу (меняет строки и столбцы местами).

    Args:
        mat: Прямоугольная матрица

    Returns:
        Транспонированная матрица

    Raises:
        ValueError: Если матрица рваная
    """
    _validate_rectangular(mat)

    if not mat:
        return []

    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Вычисляет суммы по строкам матрицы.

    Args:
        mat: Прямоугольная матрица

    Returns:
        Список сумм по строкам

    Raises:
        ValueError: Если матрица рваная
    """
    _validate_rectangular(mat)

    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Вычисляет суммы по столбцам матрицы.

    Args:
        mat: Прямоугольная матрица

    Returns:
        Список сумм по столбцам

    Raises:
        ValueError: Если матрица рваная
    """
    _validate_rectangular(mat)

    if not mat:
        return []

    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]

print("\n=== Matrix Tests ===")
print(transpose([[1, 2, 3]]))  # [[1], [2], [3]]
print(row_sums([[1, 2, 3], [4, 5, 6]]))  # [6, 15]
print(col_sums([[1, 2, 3], [4, 5, 6]]))  # [5, 7, 9]