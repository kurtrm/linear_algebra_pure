"""
Module supplying a function for matrix multiplication.
Numpy is way better, I'm strictly trying to solidify my understanding
by implementing it in Python.
"""


def multiply_matrices(m_1: list, m_2: list) -> list:
    """
    Parameters
    ----------
    m_1 : list of lists =>
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

    m_2 : list of lists =>
    [[10, 11, 12],
     [13, 14, 15],
     [17, 18, 19]]

    Returns
    ------
    transformation : list of lists =>
    [[ 87,  93,  99],
     [207, 222, 237],
     [327, 351, 375]]
    """
    if len(m_1[0]) != len(m_2):
        raise ValueError("Size mismatch: m_1 columns do not match m_2 rows")
    transformation = [[] for _ in m_1]
    for column_idx, _ in enumerate(m_2[0]):
        for i, m1_row in enumerate(m_1):
            m_2_column = [m2_row[column_idx] for m2_row in m_2]
            positional_sum = sum(a * b for a, b in zip(m1_row, m_2_column))
            transformation[i].append(positional_sum)
    return transformation
