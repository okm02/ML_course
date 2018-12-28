# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    rows = range(0,x.shape[0])
    np.random.shuffle(rows)
    train_len = int(ratio * len(rows))
    train_indices,test_indices = rows[0:train_len],rows[train_len:]
    train_data,train_target = x[train_indices],y[train_indices]
    test_data,test_target = x[test_indices],y[test_indices]

    return train_data,train_target,test_data,test_target
