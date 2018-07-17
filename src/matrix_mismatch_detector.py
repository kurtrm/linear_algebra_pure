"""
Function that takes in a bunch of numbers and determines if matrix
multiplication can occur.

1223344663322232
011111111
1, 2
1, 3
1, 4
1, 6
1, 3
1, 2
"""
from itertools import zip_longest


def can_multiply_matrices(*args):
    """
    Takes in a series of tuples and detects
    whether they can all be multiplied.
    Meant to take in a series of numpy array shapes.
    """
    rows, columns = zip(*args)
    for row, column in zip_longest(rows[1:], columns):
        if row != column:
            return row is None
