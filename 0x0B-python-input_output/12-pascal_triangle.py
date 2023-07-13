#!/usr/bin/python3
"""returns a list of lists of integers representing Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s
    triangle

    Args:
        n (int): The number of rows in the triangle

    Returns:
        list of list of int: The Pascal’s triangle 
    """
    # Returns an empty list if n <= 0
    if n <= 0:
        return []

    # Initialize the triangle with the top row
    triangle = [[1]]

    # generate the remaining rows
    for row in range(1, n):
        prev_row = triangle[row - 1]
        curr_row = [1]

        for col in range(1, row):
            curr_element = prev_row[col - 1] + prev_row[col]
            curr_row.append(curr_element)
        # add the last element to the row
        curr_row.append(1)
        triangle.append(curr_row)

        return triangle
