import numpy as np
import time

matrix = np.array(
    [(2.0, 14.0, -15.0, 23.0),
     (16.0, 2.0, -11.0, 29.0),
     (18.0, 20.0, -10.0, 22.0),
     (10.0, 12.0, -16.0, 5.0)],
    dtype=np.float64)

matrix_rez: object = np.array([5.0, 8.0, 9.0, 4.0])

matrix2 = np.array(  # matrix with diagonal predominance
    [(200.0, 1.0, 1.0, 1.0),
     (1.0, 150.0, 1.0, 1.0),
     (1.0, 1.0, 100.0, 1.0),
     (1.0, 1.0, 1.0, 50.0)],
    dtype=np.float64)


# # KRAMER METHOD
#
# # deleting rows and columns in matrix
#
# def minor(matr, k):
#     matr = np.delete(matr, k, axis=1)
#     return np.delete(matr, 0, axis=0)
#
# # recursive function for finding the determinant
#
# def det(matr):
#     n = len(matr)
#     if n == 2:
#         return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]
#     s = 0
#     z = 1
#     for i in range(n):
#         s = s + z * matr[0][i] * det(minor(matr, i))
#         z = -z
#     return s
#
# # main function
#
# def kramer(matr):
#     global i
#     d = det(matr)
#     for i in range(4):
#         new_matrix = np.copy(matr)
#         for j in range(4):
#             new_matrix[j][i] = matrix_rez[j]
#         print("x" + str(i + 1), "=", (det(new_matrix) / d))
#
# start_time = time.time()
# kramer(matrix)
# print("Task completed in %s seconds " % (time.time() - start_time))

# GAUSS METHOD


def delenie(matr, n):  # division by the main term starting from n
    for i in range(n, 4, 1):
        b = matr[i][n]
        for j in range(5):
            matr[i][j] /= b
    return matr


def razn(matr, n):  # difference of two lines
    for i in range(n + 1, 4):
        for j in range(5):
            matr[i][j] -= matr[n][j]


def main(matr):
    start_time = time.time()
    a = np.ones(4)  # forward stroke
    matr = np.c_[matr, matrix_rez]
    for n in range(4):
        delenie(matr, n)
        razn(matr, n)
    a[3] = matr[3][4]  # backwards stroke
    a[2] = -(matr[2][3] * a[3]) + matr[2][4]
    a[1] = -(matr[1][3] * a[3] + matr[1][2] * a[2]) + matr[1][4]
    a[0] = -(matr[0][3] * a[3] + matr[0][2] * a[2] + matr[0][1] * a[1]) + matr[0][4]

    for i in range(4):
        print("x" + str(i + 1), "=", a[i])
    print("Task completed in %s seconds " % (time.time() - start_time))


main(matrix)


# ITERATIONS

# def diag(matr):  # checking for diagonalizability
#     s = 0
#     for i in range(4):
#         if abs(matr[i][i]) > abs(matr[i][0]) + abs(matr[i][1]) + abs(matr[i][2]) + abs(matr[i][3]) - abs(matr[i][i]):
#             s += 1
#     if s == 4:
#         return True
#     else:
#         return False
#
#
# def main(matr):
#     if diag(matr):
#         e = 0.00001
#         res = np.ones((4, 1))  # result array
#         xn = np.ones((4, 1))  # temp array
#         for i in range(4):
#             res[i] = matrix_rez[i] / matr[i][i]
#         while True:
#             for i in range(4):
#                 xn[i] = matrix_rez[i] / matr[i][i]
#                 for j in range(4):
#                     if i == j:
#                         continue
#                     else:
#                         xn[i] -= matr[i][j] / matr[i][i] * res[j]
#             flag = True
#             for i in range(4):
#                 if abs(xn[i] - res[i]) > e:
#                     flag = False
#                     break
#             for i in range(4):
#                 res[i] = xn[i]
#             if flag:
#                 break
#         for i in range(4):
#             print("x" + str(i + 1), "=", res[i])
#         print("With accuracy", e)
#     else:
#         print("В системе не выполняется диагональное преобладание")
#
#
# start_time = time.time()
# main(matrix2)
# print("Task completed in %s seconds " % (time.time() - start_time))
