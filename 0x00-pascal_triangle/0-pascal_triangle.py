#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s
    triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(n - 1):
        row = [0] + triangle[-1] + [0]
        add_new_row = []
        for j in range(len(row) - 1):
            add_new_row.append(row[j] + row[j + 1])
        triangle.append(add_new_row)
    return triangle 
