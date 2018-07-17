"""
Contains one function that transposes a matrix.
"""
from typing import List


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    """
    rows, columns = len(matrix), len(matrix[0])
    return [[matrix[row_idx][col_idx] for row_idx in range(rows)]
            for col_idx in range(columns)]
