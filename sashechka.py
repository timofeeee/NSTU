from sympy import *
from math import *
import numpy as np
import Kramer
import time

def f_x(x, y):  # x function
    return sqrt(tan((x * y) + 0.3))


def f_y(x):  # y function
    return sqrt((1 - 0.9 * x ** 2) / 2)


def f_x_x(x, y):  # x function derivative by x
    return (y * sec(x * y + 0.4) * sec(x * y + 0.4)) / (2 * sqrt(tan(x * y + 0.4)))


def f_x_y(x, y):  # x function derivative by y
    return (x * sec(0.3 + x * y) ** 2) / (2 * sqrt(tan(0.3 + x * y)))


def f_y_x(x):  # y function derivative by x
    return (-0.636396 * x) / sqrt(1 - 0.9 * x ** 2)


def f_y_y():  # y function derivative by y
    return 0


def det(matr):
    return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]


def proverka_iter(x, y):
    if abs(f_y_x(x)) + abs(f_x_x(x, y)) < 1 and abs(f_y_y()) + abs(f_x_x(x, y)) < 1:
        return True


def proverka_newton(x, y):
    if det(Jacobian(x, y)) != 0:
        return True


def Jacobian(x, y):
    return np.array([[-2 * x + y * sec(0.3 + x * y) ** 2, x * sec(0.3 + x * y) ** 2],
                     [1.8 * x, 4 * y]])


def F(x, y):
    return np.array([[tan(x * y + 0.3) - x ** 2],
                     [(0.9 * x ** 2) + (2 * y ** 2) - 1]])


# ITER METHOD

# def main():
#     n = 0
#     e = 0.00001
#     x = [1., 0.]
#     y = [0.5, 0.]
#     if proverka_iter(x[0] - 0.1, y[0] - 0.1):
#         while True:
#             flag = False
#             n += 1
#             y[1] = f_y(x[0])
#             x[1] = f_x(x[0], y[0])
#             if max(abs(x[1] - x[0]), abs(y[1] - y[0])) < e:
#                 flag = True
#                 break
#             y[0] = y[1]
#             x[0] = x[1]
#             if flag:
#                 break
#         print("x =", x[1])
#         print("y =", y[1])
#         print("With accuracy", e, "Amount  of iterations:", n)
#     else:
#         print("The convergence condition is not met")
#
# main()


# # SEIDEL METHOD

# def main():
#     n = 0
#     e = 0.00001
#     x = [1., 0.]
#     y = [0.5, 0.]
#     if proverka_iter(x[0] - 0.1, y[0] - 0.1):  # convergence condition
#         while True:
#             flag = False
#             n += 1
#             y[1] = f_y(x[0])
#             x[1] = f_x(x[0], y[1])
#             if max(abs(x[1] - x[0]), abs(y[1] - y[0])) < e:  # exit condition
#                 flag = True
#                 break
#             y[0] = y[1]
#             x[0] = x[1]
#             if flag:
#                 break
#         print("x =", x[1])
#         print("y =", y[1])
#         print("With accuracy", e, "Amount of iterations:", n)
#     else:
#         print("The convergence condition is not met")
#
#
# main()

def newton():
    e = 0.00001
    n = 0
    x1 = [0.8, 0.]
    y1 = [0.3, 0.]

    if proverka_newton(0.8, 0.3):
        while True:
            n += 1
            x, y = Kramer.Kramer(Jacobian(x1[0], y1[0]), -1 * F(x1[0], y1[0]))
            x1[1] = x1[0] + x
            y1[1] = y1[0] + y
            if max(abs(x1[0] - x1[1]), abs(y1[0] - y1[1])) < e:
                break
            else:
                x1[0] = x1[1]
                y1[0] = y1[1]
        print("x =", x1[1], "y =", y1[1])
        print("With accuracy", e, "Amount  of iterations:", n)
    else:
        print("The convergence condition is not met")


start_time = time.time()
newton()
print("Task completed in %s seconds " % (time.time() - start_time))
