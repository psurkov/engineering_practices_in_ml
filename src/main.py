from sklearn.datasets import make_moons

from DecisionTreeClassifier import DecisionTreeClassifier
from visualization import draw_tree, plot_2d, plot_roc_curve


def main():
    noise = 0.35
    X, y = make_moons(1500, noise=noise)
    X_test, y_test = make_moons(200, noise=noise)
    tree = DecisionTreeClassifier(max_depth=5, min_samples_leaf=30)
    tree.fit(X, y)
    plot_2d(tree, X, y)
    plot_roc_curve(y_test, tree.predict_proba(X_test))
    draw_tree(tree)


if __name__ == "__main__":
    main()
