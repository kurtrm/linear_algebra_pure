"""
Use a function to find the determinants of any size matrix.
Uses raw python.

The same functionality is available in numpy.linalg.det
"""
from typing import List


def find_determinant(matrix: List[List[int]], expansion_row: int=None) -> int:
    """
    Find the determinant of an n x n matrix.

    expansion_row parameter will not change answer; it is available as proof
    that the choice of expansion_row will not change the answer.
    """
    rows, columns = len(matrix), len(matrix[0])
    if rows != columns:
        raise ValueError(f"Matrix mismatch: {columns} does not equal {rows}")
    if expansion_row is None:
        expansion_row = 0
    else:
        expansion_row -= 1
        if expansion_row > rows:
            raise ValueError("Invalid expansion_row argument")
    if rows == 1 and columns == 1:
        return matrix[0][0]
    if rows == 2 and columns == 2:
        return base_determinant(matrix)

    column = 0
    minors = []
    for _ in range(rows):
        new_matrix = []
        for i, row in enumerate(matrix):
            if i == expansion_row:
                continue
            new_matrix_row = []
            for idx, num in enumerate(row):
                if idx == column:
                    continue
                new_matrix_row.append(num)
            new_matrix.append(new_matrix_row)
        column += 1
        minor = find_determinant(new_matrix)
        minors.append(minor)
    signs = ((-1)**(row + col) for row, col in zip(repeat(expansion_row),
                                                   range(columns)))
    cofactors = [sign * minor for sign, minor in zip(signs, minors)]
    return sum(cofactor * expansion for cofactor, expansion in zip(cofactors,
                                                                   matrix[expansion_row]))


def base_determinant(matrix: List[List[int]]) -> int:
    """
    Find determinant of a 2 x 2 matrix.
    """
    if (len(matrix[0]), len(matrix)) != (2, 2):
        raise ValueError(f"Matrix mismatch: Not 2 x 2 matrix.")
    return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
