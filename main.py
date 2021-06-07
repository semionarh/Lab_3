import math
import sys


def get_det(matrix):
    det = 0
    for i in range(len(matrix)):
        comp = alg_adds(matrix, 0, i)
        if len(comp) == 0:
            det = -matrix[0][0]
        elif len(comp) == 1:
            det = (det * (-1) + matrix[0][i] * comp[0][0])
        else:
            det = det + matrix[0][i] * get_det(comp) * math.pow(-1, i + 1)
    return det * (-1)


def reverse_matrix(matrix):
    inverse_matrix = []
    det = get_det(matrix)
    if det == 0:
        print("Решений нет или их бесконечно много!")
        sys.exit()
    for i in range(len(matrix)):
        inverse_matrix.append([])
        for j in range(len(matrix[i])):
            inverse_matrix[i].append(
                (1 / det) * get_det(alg_adds(matrix, i, j)) * math.pow((-1), (j + i)))
    return transp_matrix(inverse_matrix)


def alg_adds(matrix, first_row, first_col):
    rang = len(matrix)
    new_matrix = []
    counter = -1
    for i in range(rang):
        if i != first_row:
            new_matrix.append([])
            counter += 1
        for j in range(rang):
            if i != first_row and j != first_col:
                new_matrix[counter].append(matrix[i][j])
    return new_matrix


def vector_mult(matrix, vector_arr):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(0)
        for j in range(len(matrix[i])):
            new_matrix[i] += matrix[i][j] * vector_arr[j]
    return new_matrix


def number_mult(matrix, number):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= number
    return matrix


def unknown_members(matrix, b_arr):
    det = get_det(matrix)
    if det == 0:
        print("Решений нет или их бесконечно много!")
        sys.exit()
    inverse_matrix = reverse_matrix(matrix)
    answer_vector = vector_mult(inverse_matrix, b_arr)
    return answer_vector


def transp_matrix(matrix):
    transposed_matrix = []
    for i in range(len(matrix)):
        transposed_matrix.append([])
        for j in range(len(matrix[i])):
            transposed_matrix[i].append(matrix[j][i])
    return transposed_matrix


if __name__ == '__main__':
    matrix_str = input("Введите матрицу в строку в формате, где разделение между числами-пробел\n")
    matrix_str = matrix_str.split()
    rang = math.sqrt(len(matrix_str))
    if not rang.is_integer():
        raise IOError("Матрица на квадратная")
    matrix = []
    counter = 0
    for i in range(int(rang)):
        matrix.append([])
        for j in range(int(rang)):
            matrix[i].append(int(matrix_str[counter]))
            counter += 1

    b = input("Введите свободные члены уравнения, вид уравнения A * X = B, B-вектор свободных членов\n")
    b_arr = [int(x) for x in b.split()]
    if len(b_arr) != len(matrix):
        raise IOError("Ранг матрицы и количество свободных членов должны совпадать!")
    print(unknown_members(matrix, b_arr))