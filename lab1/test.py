import numpy as np
import matplotlib.pyplot as plt

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
    return k, b, max_deviation



x1 = np.array([1, 2, 3.1, 5, 5])
y1 = np.array([2, 3.4, 4, 5, 6])
print(approximate_linear_least_modules(x1, y1)[2])

x2 = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])
y2 = np.array([2.1, 2.3, 2.6, 3.0, 3.5, 4.1, 4.8, 5.6, 6.5, 7.5, 8.6])
print(approximate_linear_least_modules(x2, y2)[2])

x3 = np.array([0.5, 1.5, 2.7, 3.5])
y3 = np.array([3, 4.8, 5.9, 7.1])
print(approximate_linear_least_modules(x3, y3)[2])

x4 = np.array([-100, -200, -300, -400, -640])
y4 = np.array([-200, -300, -400, -500, -700])
print(approximate_linear_least_modules(x4, y4)[2])

x5 = np.array([-1, -2, -3, -4, -5])
y5 = np.array([3, 4.8, 5.9, 7.1, 8])
print(approximate_linear_least_modules(x5, y5)[2])

# Example 1
plt.subplot(2, 3, 1)
plt.scatter(x1, y1, color='blue', label='Data')
k, b, _ = approximate_linear_least_modules(x1, y1)
plt.plot(x1, k * x1 + b, color='red', label='Linear Approximation')
plt.gca().set_aspect('equal', adjustable='box')

# Example 2
plt.subplot(2, 3, 2)
plt.scatter(x2, y2, color='orange', label='Data')
k, b, _ = approximate_linear_least_modules(x2, y2)
plt.plot(x2, k * x2 + b, color='red', label='Linear Approximation')
plt.gca().set_aspect('equal', adjustable='box')

# Example 3
plt.subplot(2, 3, 3)
plt.scatter(x3, y3, color='green', label='Data')
k, b, _ = approximate_linear_least_modules(x3, y3)
plt.plot(x3, k * x3 + b, color='red', label='Linear Approximation')
plt.gca().set_aspect('equal', adjustable='box')

# Example 4
plt.subplot(2, 3, 4)
plt.scatter(x4, y4, color='red', label='Data')
k, b, _ = approximate_linear_least_modules(x4, y4)
plt.plot(x4, k * x4 + b, color='red', label='Linear Approximation')
plt.gca().set_aspect('equal', adjustable='box')

# Example 5
plt.subplot(2, 3, 5)
plt.scatter(x5, y5, color='purple', label='Data')
k, b, _ = approximate_linear_least_modules(x5, y5)
plt.plot(x5, k * x5 + b, color='red', label='Linear Approximation')
plt.gca().set_aspect('equal', adjustable='box')

# Show plots
plt.tight_layout()
plt.show()