#!/usr/bin/python3

"""A Module containing a function that multiplies 2 matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): the first matrix.
        m_b (list of lists of ints/floats): the second matrix.
    """

    return (np.matmul(m_a, m_b))
