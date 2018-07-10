"""
Contains one function that transposes a matrix.
"""
from typing import List


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    """
    rows, columns = len(matrix), len(matrix[0])
    transposed_matrix = []
    for col_idx in range(columns):
        new_row = []
        for row_idx in range(rows):
            new_row.append(matrix[row_idx][col_idx])
        transposed_matrix.append(new_row)

    return transposed_matrix
