from typing import Union

import numpy as np


class DecisionTreeLeaf:
    """

    Attributes
    ----------
    y : Тип метки (напр., int или str)
        Метка класса, который встречается чаще всего среди элементов листа дерева
    """

    def __init__(self, labels: np.ndarray):
        ys, counts = np.unique(labels, return_counts=True)
        self.y = ys[np.argmax(counts)]
        proportion = counts / labels.shape[0]
        self.probs = dict(zip(ys, proportion))


class DecisionTreeNode:
    """

    Attributes
    ----------
    split_dim : int
        Измерение, по которому разбиваем выборку.
    split_value : float
        Значение, по которому разбираем выборку.
    left : Union[DecisionTreeNode, DecisionTreeLeaf]
        Поддерево, отвечающее за случай x[split_dim] < split_value.
    right : Union[DecisionTreeNode, DecisionTreeLeaf]
        Поддерево, отвечающее за случай x[split_dim] >= split_value.
    """

    def __init__(
        self,
        split_dim: int,
        split_value: float,
        left: Union["DecisionTreeNode", DecisionTreeLeaf],
        right: Union["DecisionTreeNode", DecisionTreeLeaf],
    ):
        self.split_dim = split_dim
        self.split_value = split_value
        self.left = left
        self.right = right
