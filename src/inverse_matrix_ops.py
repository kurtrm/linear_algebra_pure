"""
Contains functions that conduct operations centered around finding
the inverse of a matrix.
"""
from itertools import repeat
from typing import List

from determinants import base_determinant, find_determinant
from tranpose import transpose_matrix


def find_adjoint(matrix: List[List[int]]) -> List[List[int]]:
    """
    Find the adjoint of a matrix.
    """
    rows, columns = len(matrix), len(matrix[0])
    expansion_row = 0
    adjoint_matrix = []
    for _ in range(rows):
        minors = []
        skip = 0
        for _ in range(rows):
            new_matrix = []
            for i, row in enumerate(matrix):
                if i == expansion_row:
                    continue
                new_matrix_row = []
                for idx, num in enumerate(row):
                    if idx == skip:
                        continue
                    new_matrix_row.append(num)
                new_matrix.append(new_matrix_row)
            skip += 1
            minor = find_determinant(new_matrix)
            minors.append(minor)
        signs = ((-1)**(row + col) for row, col in zip(repeat(expansion_row),
                                                       range(columns)))
        cofactors = [sign * minor for sign, minor in zip(signs, minors)]
        adjoint_matrix.append(cofactors)
        expansion_row += 1

    return transpose_matrix(adjoint_matrix)


def find_inverse(matrix: List[List[int]]) -> List[List[int]]:
    """
    Find the inverse of any size n x n matrix.
    """
    rows, columns = len(matrix), len(matrix[0])
    if rows != columns:
        raise ValueError(f"Matrix mismatch: {columns} does not equal {rows}")
    if rows == 2 and columns == 2:
        return [[(1 / base_determinant(matrix)) * num
                 for num in row]
                for row in find_adjoint(matrix)]
    determinant = find_determinant(matrix)
    return [[(1 / determinant) * num
             for num in row]
            for row in find_adjoint(matrix)]
