from math import *

import numpy as np
from sympy import *

import Kramer
import time


# ITERATIONS

class Fun:

    def __init__(self):
        pass

    @staticmethod
    def f_x(x, y):
        return sqrt(tan(x * y + 0.4))

    @staticmethod
    def f_y(x):
        return sqrt((1 - 0.6 * x ** 2) / 2)

    @staticmethod
    def f_x_x(x, y):
        return (y * sec(x * y + 0.4) * sec(x * y + 0.4)) / (2 * sqrt(tan(x * y + 0.4)))

    @staticmethod
    def f_x_y(x, y):
        return (x * sec(x * y + 0.4) * sec(x * y + 0.4)) / (2 * sqrt(tan(x * y + 0.4)))

    @staticmethod
    def f_y_x(x):
        return (-0.424264 * x) / sqrt(1 - 0.6 * x ** 2)

    @staticmethod
    def f_y_y():
        return 0


    @staticmethod
    def Jacobian(x, y):
        return np.array([[-2 * x + y * sec(0.4 + x * y ** 2), x * sec(0.4 + x * y) ** 2],
                         [1.2 * x, 4 * y]])

    @staticmethod
    def F(x, y):
        return np.array([[tan(x * y + 0.4) - x ** 2],
                         [(0.6 * x ** 2) + (2 * y ** 2) - 1]])


class Met:

    def __init__(self):
        pass


    @staticmethod
    def det(matr):
        return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]


    @staticmethod
    def proverka_iter(x, y):
        if abs(Fun.f_y_x(x)) + abs(Fun.f_x_x(x, y)) < 1 and abs(Fun.f_y_y()) + abs(Fun.f_x_x(x, y)) < 1:
            return True

    @staticmethod
    def proverka_newton(x, y):
        if Met.det(Fun.Jacobian(x, y)) != 0:
            return True


# ITER METHOD

def main():
    n = 0
    e = 0.00001
    x = [1.1, 0.]
    y = [0.4, 0.]
    if Met.proverka_iter(x[0] - 0.1, y[0] - 0.1):
        while True:
            flag = False
            n += 1
            y[1] = Fun.f_y(x[0])
            x[1] = Fun.f_x(x[0], y[0])
            if max(abs(x[1] - x[0]), abs(y[1] - y[0])) < e:
                flag = True
                break
            y[0] = y[1]
            x[0] = x[1]
            if flag:
                break
        print("x =", x[1], n)
        print("y =", y[1], n)
        print("With accuracy", e, "Amount  of iterations:",n)
    else:
        print("The convergence condition is not met")


start_time = time.time()
main()
print("Task completed in %s seconds " % (time.time() - start_time))

# # SEIDEL METHOD

# def main():
#     n = 0
#     e = 0.00001
#     x = [1.1, 0.]
#     y = [0.4, 0.]
#     if Met.proverka_iter(x[0] - 0.1, y[0] - 0.1):
#         while True:
#             flag = False
#             n += 1
#             y[1] = Fun.f_y(x[0])
#             x[1] = Fun.f_x(x[0], y[1])
#             if max(abs(x[1] - x[0]), abs(y[1] - y[0])) < e:
#                 flag = True
#                 break
#             y[0] = y[1]
#             x[0] = x[1]
#             if flag:
#                 break
#         print("x =", x[1], n)
#         print("y =", y[1], n)
#         print("With accuracy", e, "Amount of iterations:", n)
#     else:
#         print("The convergence condition is not met")
#
#
# start_time = time.time()
# main()
# print("Task completed in %s seconds " % (time.time() - start_time))

# NEWTON

# def newton():
#     e = 0.00001
#     n = 0
#     x1 = [1.1, 0.]
#     y1 = [0.4, 0.]
#
#     if Met.proverka_newton(1.1, 0.4):
#         while True:
#             n += 1
#             x, y = Kramer.Kramer(Fun.Jacobian(x1[0], y1[0]), -1 * Fun.F(x1[0], y1[0]))
#             x1[1] = x1[0] + x
#             y1[1] = y1[0] + y
#             if max(abs(x1[0] - x1[1]), abs(y1[0] - y1[1])) < e:
#                 break
#             else:
#                 x1[0] = x1[1]
#                 y1[0] = y1[1]
#         print("x =", x1[1], "y =", y1[1])
#         print("With accuracy", e, "Amount  of iterations:", n)
#     else:
#         print("The convergence condition is not met")
#
#
# start_time = time.time()
# newton()
# print("Task completed in %s seconds " % (time.time() - start_time))
