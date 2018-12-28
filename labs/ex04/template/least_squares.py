# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    # ***************************************************
    closed_form_sol = np.dot(np.dot(np.linalg.inv(np.dot(tx.T,tx)),tx.T),y)
    
    return closed_form_sol
