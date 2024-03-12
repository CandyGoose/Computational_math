#!/bin/python3

import math
import os
import random
import re
import sys


def first_function(args: []) -> float:
    return math.sin(args[0])


def second_function(args: []) -> float:
    return (args[0] * args[1]) / 2


def third_function(args: []) -> float:
    return pow(args[0], 2) * pow(args[1], 2) - 3 * pow(args[0], 3) - 6 * pow(args[1], 3) + 8


def fourth_function(args: []) -> float:
    return pow(args[0], 4) - 9 * args[1] + 2


def fifth_function(args: []) -> float:
    return args[0] + pow(args[0], 2) - 2 * args[1] * args[2] - 0.1


def six_function(args: []) -> float:
    return args[1] + pow(args[1], 2) + 3 * args[0] * args[2] + 0.2


def seven_function(args: []) -> float:
    return args[2] + pow(args[2], 2) + 2 * args[0] * args[1] - 0.3


def default_function(args: []) -> float:
    return 0.0


# How to use this function:
# funcs = Result.get_functions(4)
# funcs[0](0.01)
def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        return [third_function, fourth_function]
    elif n == 3:
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]

#
# Complete the 'solve_by_fixed_point_iterations' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER system_id
#  2. INTEGER number_of_unknowns
#  3. DOUBLE_ARRAY initial_approximations
#

def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    max_iterations = 100
    tolerance = 1e-5
    step_length = 0.0001

    def fixed_point_iteration(func, initial_guesses, max_iter, tol, step_length):
        iterations = 0
        x_prev = initial_guesses
        while iterations < max_iter:
            x_next = func(x_prev, step_length)
            if all(abs(x_next[i] - x_prev[i]) < tol for i in range(number_of_unknowns)):
                break
            x_prev = x_next
            iterations += 1
        return x_next, iterations

    functions = get_functions(system_id)

    def system(x, step_length):
        return [x[i] - step_length * functions[i](x) for i in range(number_of_unknowns)]

    solution, iterations = fixed_point_iteration(system, initial_approximations, max_iterations, tolerance, step_length)
    return solution


if __name__ == '__main__':
    system_id = int(input().strip())
    number_of_unknowns = int(input().strip())

    initial_approximations = []

    for _ in range(number_of_unknowns):
        initial_approximations_item = float(input().strip())
        initial_approximations.append(initial_approximations_item)

    result = solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations)

    print('\n'.join(map(str, result)))


