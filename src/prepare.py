import os

import numpy
from sklearn.datasets import make_moons
import dvc.api


def main():
    params = dvc.api.params_show()
    numpy.random.seed(params["prepare"]["seed"])

    noise = params["prepare"]["data"]["noise"]

    X, y = make_moons(params["prepare"]["data"]["train"]["n_samples"], noise=noise)
    X_test, y_test = make_moons(
        params["prepare"]["data"]["test"]["n_samples"], noise=noise
    )

    os.mkdir("data")
    numpy.savetxt("data/trainX.csv", X, delimiter=",")
    numpy.savetxt("data/trainY.csv", y, delimiter=",")
    numpy.savetxt("data/testX.csv", X_test, delimiter=",")
    numpy.savetxt("data/testY.csv", y_test, delimiter=",")


if __name__ == "__main__":
    main()
