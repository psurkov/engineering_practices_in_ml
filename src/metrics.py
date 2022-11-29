from typing import Callable

import numpy as np


def gini(x: np.ndarray) -> float:
    """
    Считает коэффициент Джини для массива меток x.
    """
    _, counts = np.unique(x, return_counts=True)
    p = counts / x.shape[0]
    return np.dot(p, 1 - p)


def entropy(x: np.ndarray) -> float:
    """
    Считает энтропию для массива меток x.
    """
    _, counts = np.unique(x, return_counts=True)
    p = counts / x.shape[0]
    return -np.dot(p, np.log2(p))


def gain(left_y: np.ndarray, right_y: np.ndarray, criterion: Callable) -> float:
    """
    Считает информативность разбиения массива меток.

    Parameters
    ----------
    left_y : np.ndarray
        Левая часть разбиения.
    right_y : np.ndarray
        Правая часть разбиения.
    criterion : Callable
        Критерий разбиения.
    """
    both = np.concatenate([left_y, right_y])
    both_sz = both.shape[0]
    left_sz = left_y.shape[0]
    right_sz = right_y.shape[0]
    return (
        criterion(both)
        - left_sz / both_sz * criterion(left_y)
        - right_sz / both_sz * criterion(right_y)
    )
