"""
Contains functions that conduct operations centered around finding
the inverse of a matrix.
"""
from itertools import repeat
from typing import List

from determinants import (base_determinant,
                          find_determinant,
                          find_row_cofactors)
from transpose import transpose_matrix


def find_adjoint(matrix: List[List[int]]) -> List[List[int]]:
    """
    Find the adjoint of a matrix.
    """
    rows = len(matrix)
    adjoint_matrix = []
    for iteration in range(rows):
        cofactors = find_row_cofactors(matrix, iteration)
        adjoint_matrix.append(cofactors)

    return transpose_matrix(adjoint_matrix)


def find_inverse(matrix: List[List[int]]) -> List[List[int]]:
    """
    Find the inverse of any size n x n matrix.
    """
    rows, columns = len(matrix), len(matrix[0])
    if rows != columns:
        raise ValueError(f"Matrix mismatch: {columns} does not equal {rows}")
    if rows == 2 and columns == 2:
        determinant = base_determinant(matrix)
    else:
        determinant = find_determinant(matrix)
    return [[(1 / determinant) * num for num in row]
            for row in find_adjoint(matrix)]
