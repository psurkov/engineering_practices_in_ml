import dvc.api
import numpy

from DecisionTreeClassifier import DecisionTreeClassifier
from visualization import draw_tree, plot_2d, plot_roc_curve


def main():
    X = numpy.genfromtxt("../data/trainX.csv", delimiter=",")
    y = numpy.genfromtxt("../data/trainY.csv",  delimiter=",")
    X_test = numpy.genfromtxt("../data/testX.csv", delimiter=",")
    y_test = numpy.genfromtxt("../data/testY.csv",  delimiter=",")

    params = dvc.api.params_show()
    max_depth = params["train"]["max_depth"]
    min_samples_leaf = params["train"]["min_samples_leaf"]
    tree = DecisionTreeClassifier(max_depth=max_depth, min_samples_leaf=min_samples_leaf)

    numpy.random.seed(params["train"]["seed"])

    tree.fit(X, y)

    artifacts_path = "../artifacts/"
    plot_2d(tree, X, y, artifacts_path + "plot.png")
    plot_roc_curve(y_test, tree.predict_proba(X_test), artifacts_path + "roc_curve.png")
    draw_tree(tree, artifacts_path + "tree.png")


if __name__ == "__main__":
    main()
