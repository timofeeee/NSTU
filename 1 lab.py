from time import time

#МЕТОД ПОЛОВИННОГО ДЕЛЕНИЯ


# import math
#
# a, b, e = 0.0, 1.0, 0.00001
# n = 0
# def f(x):
#     return x ** 4 - 18 * (x ** 2) + 6
#
# def half(a, b):
#     return (a + b)/2
#
# if f(a) * f(b) > 0:
#     print("no roots")
# else:
#     while abs(a - b) > e:
#         n += 1
#         x = half(a, b)
#         if f(x) * f(b) < 0:
#             a = x
#         else:
#             b = x
# print(n, "- amount of iterations")
# print("root", x, "with accuracy", e)

#МЕТОД ХОРД

# import math
#
# a, b, e = 0.0, 1.0, 0.00001
# n = 0
# def f(x):
#     return x ** 4 - 18 * (x ** 2) + 6
#
# def tochka_hordi(a, b):
#     return a - f(a)*(b - a)/(f(b) - f(a))
#
# if f(a) * f(b) > 0:
#     print("no roots")
# else:
#     while abs(a - b) > e:
#         n += 1
#         x = tochka_hordi(a, b)
#         if f(x) * f(b) < 0:
#             a = x
#         else:
#             b = x
# print(n, "- amount of iterations")
# print("root", x, "with accuracy", e)

#МЕТОД НЬЮТОНА
#
from scipy.misc import derivative


def der(f, x):
    return derivative(f, x, n=1)


def sder(f, x):
    return derivative(f, x, n=2)


def f(x):
    return x ** 4 - 18 * (x ** 2) + 6


def newton(f, a, b, e):
    global n
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        print("no roots")
    if fb * sder(f, b) > 0:
        x0 = b
    else:
        x0 = a
    while True:
        n += 1
        x = x0 - f(x0) / der(f, x0)
        if abs(x - x0) < e:
            return x
        x0 = x


n = 0
a = 1.0
b = 0.0
e = 0.00001


root = newton(f, a, b, e)
print(n, "- amount of iterations")
print("root", root, "with accuracy", e)

