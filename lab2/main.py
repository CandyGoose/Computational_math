#!/bin/python3

import math
import os
import random
import re
import sys

class Result:
    isMethodApplicable = True
    errorMessage = ""

    #
    # Complete the 'solveBySimpleIterations' function below.
    #
    # The function is expected to return a DOUBLE_ARRAY.
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. 2D_DOUBLE_ARRAY matrix
    #  3. DOUBLE epsilon
    #

    @staticmethod
    def check_diagonal_dominance(matrix):
        n = len(matrix)
        for i in range(n):
            row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
            if abs(matrix[i][i]) <= row_sum:
                return False
        return True

    @staticmethod
    def solveBySimpleIterations(n, matrix, epsilon):
        if not Result.check_diagonal_dominance(matrix):
            Result.isMethodApplicable = False
            Result.errorMessage = "The system has no diagonal dominance for this method. Method of the simple iterations is not applicable."
            return None

        x = [0.0] * n
        prev_x = [0.0] * n
        max_iterations = 1000
        iteration = 0
        while iteration < max_iterations:
            for i in range(n):
                sum_term = sum(matrix[i][j] * x[j] for j in range(n) if j != i)
                x[i] = (matrix[i][n] - sum_term) / matrix[i][i]

            max_diff = max(abs(x[i] - prev_x[i]) for i in range(n))
            if max_diff < epsilon:
                break

            prev_x = x.copy()
            iteration += 1

        return x

if __name__ == '__main__':

    n = int(input().strip())

    matrix_rows = n
    matrix_columns = n+1

    matrix = []

    for _ in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))

    epsilon = float(input().strip())

    result = Result.solveBySimpleIterations(n, matrix, epsilon)
    if Result.isMethodApplicable:
        print('\n'.join(map(str, result)))
    else:
        print(f"{Result.errorMessage}")
