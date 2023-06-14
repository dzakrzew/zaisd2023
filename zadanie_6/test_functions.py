
import math

def rastragin_fun(X):
    return 10 * len(X) + sum(map(lambda x: x ** 2 - 10 * math.cos(2 * math.pi * x), X))


def rosenbrock_fun(X):
    _sum = 0
    length = len(X)

    for i in range(length - 1):
        _sum += 100 * (X[i + 1] - X[i] ** 2) ** 2 + (X[i] - 1) ** 2

    return _sum


def hyper_ellipsoid_fun(X):
    length = len(X)
    return sum([(i + 1) * X[i] ** 2 for i in range(length)])


def shubert_fun(X):
    sum_1 = 0
    sum_2 = 0
    for i in range(len(X)):
        for j in range(5):
            term_1 = (j + 1) * math.cos((j + 2) * X[i] + (j + 1))
            term_2 = math.cos((j + 2) * X[i] + (j + 1))
            sum_1 += term_1
            sum_2 += term_2
    return sum_1 * sum_2


def sphere_fun(X):
    return sum(map(lambda x: x ** 2, X))


def sum_squares_fun(X):
    return sum([(i + 1) * X[i] ** 2 for i in range(len(X))])


def styblinski_tang_fun(X):
    _sum = 0
    for i in range(len(X)):
        _sum += X[i] ** 4 - 16 * X[i] ** 2 + 5 * X[i]
    return 0.5 * _sum


def weierstrass_fun(X):
    return sum(map(lambda x: (x + 0.5) ** 2, X))