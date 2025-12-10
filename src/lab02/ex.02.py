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
            raise ValueError(
                f"Матрица рваная: строка {i} имеет длину {len(row)}, ожидалась {first_len}"
            )


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

# Тест 1: нормальное транспонирование
print("transpose([[1, 2, 3]]):", transpose([[1, 2, 3]]))  # [[1], [2], [3]]

# Тест 2: транспонирование рваной матрицы
try:
    print("transpose([[1, 2], [3]]):", transpose([[1, 2], [3]]))
except ValueError as e:
    print(f"transpose([[1, 2], [3]]): ValueError - {e}")

# Тест 3: транспонирование пустой матрицы
print("transpose([]):", transpose([]))  # []

# Тест 4: суммы по строкам
print("row_sums([[1, 2, 3], [4, 5, 6]]):", row_sums([[1, 2, 3], [4, 5, 6]]))  # [6, 15]

# Тест 5: суммы по строкам рваной матрицы
try:
    print("row_sums([[1, 2], [3]]):", row_sums([[1, 2], [3]]))
except ValueError as e:
    print(f"row_sums([[1, 2], [3]]): ValueError - {e}")

# Тест 6: суммы по столбцам
print(
    "col_sums([[1, 2, 3], [4, 5, 6]]):", col_sums([[1, 2, 3], [4, 5, 6]])
)  # [5, 7, 9]

# Тест 7: суммы по столбцам рваной матрицы
try:
    print("col_sums([[1, 2], [3]]):", col_sums([[1, 2], [3]]))
except ValueError as e:
    print(f"col_sums([[1, 2], [3]]): ValueError - {e}")

# Тест 8: дополнительные тесты
print("transpose([[1, 2], [3, 4]]):", transpose([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print("row_sums([[-1, 1], [10, -10]]):", row_sums([[-1, 1], [10, -10]]))  # [0, 0]
print("col_sums([[-1, 1], [10, -10]]):", col_sums([[-1, 1], [10, -10]]))  # [9, -9]
