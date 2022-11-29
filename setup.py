import setuptools

setuptools.setup(
    name="homework_test_package_2",
    version="1.0",
    install_requires=[
        "numpy==1.23.5",
        "pandas==1.5.1",
        "matplotlib==3.6.2",
        "scikit-learn==1.1.3",
        "build==0.9.0",
    ],
    packages=["src"],
)
