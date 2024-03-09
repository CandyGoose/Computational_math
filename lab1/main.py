#
# Complete the 'approximate_linear_least_modules' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. DOUBLE_ARRAY x_axis
#  2. DOUBLE_ARRAY y_axis
#

def weighted_abs_sum(x, y, w):
    return sum(w[i] * abs(y[i] - x[i]) for i in range(len(x)))

def approximate_linear_least_modules(x, y):
    n = len(x)
    weights = [1] * n
    epsilon = 1e-5
    max_iterations = 1000
    k = 0
    b = 0
    for _ in range(max_iterations):
        k_prev = k
        b_prev = b
        sumPXY = sum(weights[i] * x[i] * y[i] for i in range(n))
        sumPX = sum(weights[i] * x[i] for i in range(n))
        sumPY = sum(weights[i] * y[i] for i in range(n))
        sumPX2 = sum(weights[i] * x[i] * x[i] for i in range(n))
        sumP = sum(weights)
        k = (sumPXY * sumP - (sumPX * sumPY)) / (sumPX2 * sumP - sumPX * sumPX)
        b = (sumPY - k * sumPX) / sumP
        for i in range(n):
            weights[i] = 1 / (abs(y[i] - b - k * x[i]) + epsilon)
        if abs(k - k_prev) < epsilon and abs(b - b_prev) < epsilon:
            break

    max_deviation = max(abs(y[i] - (b + k * x[i])) for i in range(n))
    return max_deviation

if __name__ == '__main__':
    axis_count = int(input().strip())

    x_axis = list(map(float, input().rstrip().split()))

    y_axis = list(map(float, input().rstrip().split()))

    result = approximate_linear_least_modules(x_axis, y_axis)

    print(str(result) + '\n')