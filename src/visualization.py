import numpy as np
from matplotlib import pyplot as plt

from DecisionTree import DecisionTreeNode


def tree_depth(tree_root):
    if isinstance(tree_root, DecisionTreeNode):
        return max(tree_depth(tree_root.left), tree_depth(tree_root.right)) + 1
    return 1


def draw_tree_rec(tree_root, x_left, x_right, y):
    x_center = (x_right - x_left) / 2 + x_left
    if isinstance(tree_root, DecisionTreeNode):
        x_center = (x_right - x_left) / 2 + x_left
        x = draw_tree_rec(tree_root.left, x_left, x_center, y - 1)
        plt.plot((x_center, x), (y - 0.1, y - 0.9), c=(0, 0, 0))
        x = draw_tree_rec(tree_root.right, x_center, x_right, y - 1)
        plt.plot((x_center, x), (y - 0.1, y - 0.9), c=(0, 0, 0))
        plt.text(
            x_center,
            y,
            "x[%i] < %f" % (tree_root.split_dim, tree_root.split_value),
            horizontalalignment="center",
        )
    else:
        plt.text(x_center, y, str(tree_root.y), horizontalalignment="center")
    return x_center


def draw_tree(tree, save_path=None):
    td = tree_depth(tree.root)
    plt.figure(figsize=(0.33 * 2**td, 2 * td))
    plt.xlim(-1, 1)
    plt.ylim(0.95, td + 0.05)
    plt.axis("off")
    draw_tree_rec(tree.root, -1, 1, td)
    plt.tight_layout()
    if save_path is not None:
        plt.savefig(save_path)
    plt.show()


def plot_roc_curve(y_test, p_pred):
    positive_samples = sum(1 for y in y_test if y == 0)
    tpr = []
    fpr = []
    for w in np.arange(-0.01, 1.02, 0.01):
        tpr_cnt, fpr_cnt = get_tpr_fpr(p_pred, w, y_test)

        tpr.append(tpr_cnt / positive_samples)
        fpr.append(fpr_cnt / (len(y_test) - positive_samples))
    plt.figure(figsize=(7, 7))
    plt.plot(fpr, tpr)
    plt.plot([0, 1], [0, 1], linestyle="--")
    plt.xlabel("False positive rate")
    plt.ylabel("True positive rate")
    plt.xlim(-0.01, 1.01)
    plt.ylim(-0.01, 1.01)
    plt.tight_layout()
    plt.show()


def get_tpr_fpr(p_pred, w, y_test):
    y_pred = pred_to_y(p_pred, w)

    ys = []
    for (yp, yt) in zip(y_pred, y_test):
        if yp == 0:
            ys.append(yt)
    return len([x for x in ys if x == 0]), len([x for x in ys if x != 0])


def pred_to_y(p_pred, w):
    y_pred = []
    for p in p_pred:
        if p.get(0, 0) > w:
            y = 0
        else:
            y = 1
        y_pred.append(y)
    return y_pred


def rectangle_bounds(bounds):
    return (
        (bounds[0][0], bounds[0][0], bounds[0][1], bounds[0][1]),
        (bounds[1][0], bounds[1][1], bounds[1][1], bounds[1][0]),
    )


def plot_2d_tree(tree_root, bounds, colors):
    if not isinstance(tree_root, DecisionTreeNode):
        x, y = rectangle_bounds(bounds)
        plt.fill(x, y, c=colors[tree_root.y] + [0.2])
        return

    first_bound = bounds[0]
    second_bound = bounds[1]
    if tree_root.split_dim:
        plot_2d_tree(
            tree_root.left,
            [first_bound, [second_bound[0], tree_root.split_value]],
            colors,
        )
        plot_2d_tree(
            tree_root.right,
            [first_bound, [tree_root.split_value, second_bound[1]]],
            colors,
        )
        plt.plot(
            first_bound, (tree_root.split_value, tree_root.split_value), c=(0, 0, 0)
        )
    else:
        plot_2d_tree(
            tree_root.left,
            [[first_bound[0], tree_root.split_value], second_bound],
            colors,
        )
        plot_2d_tree(
            tree_root.right,
            [[tree_root.split_value, first_bound[1]], second_bound],
            colors,
        )
        plt.plot(
            (tree_root.split_value, tree_root.split_value), second_bound, c=(0, 0, 0)
        )


def get_random_color():
    return list(np.random.random(3))


def plot_2d(tree, X, y):
    plt.figure(figsize=(9, 9))
    unique_classes = np.unique(y)
    colors = {c: get_random_color() for c in unique_classes}
    bounds = list(zip(np.min(X, axis=0), np.max(X, axis=0)))
    plt.xlim(*bounds[0])
    plt.ylim(*bounds[1])
    plot_2d_tree(tree.root, list(zip(np.min(X, axis=0), np.max(X, axis=0))), colors)
    for c in unique_classes:
        plt.scatter(X[y == c, 0], X[y == c, 1], c=[colors[c]], label=c)
    plt.legend()
    plt.tight_layout()
    plt.show()
