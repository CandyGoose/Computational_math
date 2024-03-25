import math
import numpy as np
import matplotlib.pyplot as plt

class Result:
    error_message = ""
    has_discontinuity = False
    eps = 1e-5

    def first_function(x: float):
        return 1 / x

    def second_function(x):
        if isinstance(x, np.ndarray):
            result = np.where(x == 0, (np.sin(Result.eps) / Result.eps + np.sin(-Result.eps) / -Result.eps) / 2,
                              np.sin(x) / x)
            return result
        else:
            if x == 0:
                return (math.sin(Result.eps) / Result.eps + math.sin(-Result.eps) / -Result.eps) / 2
            return math.sin(x) / x

    def third_function(x: float):
        return x * x + 2

    def fourth_function(x: float):
        return 2 * x + 2

    def five_function(x):
        return np.log(x) if isinstance(x, np.ndarray) else math.log(x) if x > 0 else math.inf

    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    def get_function(n: int):
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        elif n == 5:
            return Result.five_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")

    #
    # Complete the 'calculate_integral' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. DOUBLE a
    #  2. DOUBLE b
    #  3. INTEGER f
    #  4. DOUBLE epsilon
    #

    def calculate_integral(a, b, f, epsilon):
        func = Result.get_function(f)
        n = 1
        integral_old = 0
        while True:
            h = (b - a) / n
            integral_new = 0.5 * (func(a) + func(b))
            for i in range(1, n):
                integral_new += func(a + i * h)
            integral_new *= h
            if abs(integral_new - integral_old) < epsilon:
                return integral_new
            integral_old = integral_new
            n *= 2

            x_values = [a + i * h for i in range(n + 1)]
            for x in x_values:
                if math.isnan(func(x)) or math.isinf(func(x)):
                    Result.has_discontinuity = True
                    Result.error_message = "Integrated function has discontinuity or does not defined in current interval"
                    return 0

    @staticmethod
    def plot_function(a, b, f, epsilon):
        func = Result.get_function(f)
        x = np.linspace(a, b, 400)
        y = func(x)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)
        plt.gca().set_aspect('equal')
        plt.show()

        integral = Result.calculate_integral(a, b, f, epsilon)
        if not Result.has_discontinuity:
            print("Integral:", integral)
        else:
            print(Result.error_message)

if __name__ == '__main__':
    a = float(input().strip())

    b = float(input().strip())

    f = int(input().strip())

    epsilon = float(input().strip())

    result = Result.calculate_integral(a, b, f, epsilon)
    if not Result.has_discontinuity:
        print(str(result) + '\n')
    else:
        print(Result.error_message + '\n')

    Result.plot_function(a, b, f, epsilon)
