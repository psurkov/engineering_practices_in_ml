from typing import Any, Dict, List, NoReturn, Optional, Tuple, Union

import numpy as np

from DecisionTree import DecisionTreeLeaf, DecisionTreeNode
from metrics import entropy, gain, gini


class DecisionTreeClassifier:
    """
    Attributes
    ----------
    root : Union[DecisionTreeNode, DecisionTreeLeaf]
        Корень дерева.

    """

    def __init__(
        self,
        criterion: str = "gini",
        max_depth: Optional[int] = None,
        min_samples_leaf: int = 1,
    ):
        """
        Parameters
        ----------
        criterion : str
            Задает критерий, который будет использоваться при построении дерева.
            Возможные значения: "gini", "entropy".
        max_depth : Optional[int]
            Ограничение глубины дерева. Если None - глубина не ограничена.
        min_samples_leaf : int
            Минимальное количество элементов в каждом листе дерева.

        """
        self.root = None
        if criterion == "gini":
            self.criterion = gini
        elif criterion == "entropy":
            self.criterion = entropy
        else:
            raise NotImplementedError()
        self.max_depth = max_depth if max_depth is not None else float("inf")
        self.min_samples_leaf = min_samples_leaf

    def fit(self, X: np.ndarray, y: np.ndarray) -> NoReturn:
        """
        Строит дерево решений по обучающей выборке.

        Parameters
        ----------
        X : np.ndarray
            Обучающая выборка.
        y : np.ndarray
            Вектор меток классов.
        """
        self.root = self.__build_tree(X, y, 0)

    def __build_tree(
        self, X: np.ndarray, y: np.ndarray, depth: int
    ) -> Union[DecisionTreeNode, DecisionTreeLeaf]:
        if depth >= self.max_depth:
            return DecisionTreeLeaf(y)
        bests = np.array(
            [self.__find_best_split_value(k, X, y) for k in range(X.shape[1])]
        )
        k = np.argmax(bests, axis=0)[0]
        value = bests[k][1]
        left_X, left_y, right_X, right_y = self.__partition(k, value, X, y)
        if min(left_y.shape[0], right_y.shape[0]) < self.min_samples_leaf:
            return DecisionTreeLeaf(y)
        return DecisionTreeNode(
            k,
            value,
            self.__build_tree(left_X, left_y, depth + 1),
            self.__build_tree(right_X, right_y, depth + 1),
        )

    def __find_best_split_value(
        self, k: int, X: np.ndarray, y: np.ndarray
    ) -> Tuple[float, float]:
        """
        Возвращает лучший gain и значение по которому для этого надо разделять
        """
        x = X[:, k]
        sorted_indexes = np.argsort(x)
        x_sorted = x[sorted_indexes]
        y_sorted = y[sorted_indexes]
        max_gain = float("-inf")
        value = 0
        for i in range(1, y_sorted.shape[0]):
            g = gain(y_sorted[:i], y_sorted[i:], self.criterion)
            if g > max_gain:
                max_gain = g
                value = (x_sorted[i - 1] + x_sorted[i]) / 2
        return max_gain, value

    def __partition(
        self, k: int, value: float, X: np.ndarray, y: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Делит по k-ому признаку и значению value X и y на две части
        """
        left_ind = (X[:, k] < value).nonzero()
        right_ind = (X[:, k] >= value).nonzero()
        return X[left_ind], y[left_ind], X[right_ind], y[right_ind]

    def predict_proba(self, X: np.ndarray) -> List[Dict[Any, float]]:
        """
        Предсказывает вероятность классов для элементов из X.

        Parameters
        ----------
        X : np.ndarray
            Элементы для предсказания.

        Return
        ------
        List[Dict[Any, float]]
            Для каждого элемента из X возвращает словарь
            {метка класса -> вероятность класса}.
        """
        return [self.__predict_proba(x, self.root) for x in X]

    def __predict_proba(
        self, x: np.ndarray, cur: Union[DecisionTreeNode, DecisionTreeLeaf]
    ) -> Dict[Any, float]:
        if isinstance(cur, DecisionTreeLeaf):
            return cur.probs
        if x[cur.split_dim] < cur.split_value:
            return self.__predict_proba(x, cur.left)
        else:
            return self.__predict_proba(x, cur.right)

    def predict(self, X: np.ndarray) -> list:
        """
        Предсказывает классы для элементов X.

        Parameters
        ----------
        X : np.ndarray
            Элементы для предсказания.

        Return
        ------
        list
            Вектор предсказанных меток для элементов X.
        """
        proba = self.predict_proba(X)
        return [max(p.keys(), key=lambda k: p[k]) for p in proba]
