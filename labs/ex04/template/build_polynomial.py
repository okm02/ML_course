# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    poly_matrix = []
    for i in range(1,degree+1):
        poly_matrix.append(np.power(x,i))
    
    poly_matrix = np.asarray(poly_matrix)
    return poly_matrix.T
