import math


def factorial(x):
    result = 1
    for i in range(x):
        result *= (i + 1)
    return result


def approx_sin(x, n):
    result = 0
    for i in range(n):
        result += ((- 1) ** i) * (x ** (2*i + 1)) / factorial(2*i + 1)
    return result


def approx_cos(x, n):
    result = 0
    for i in range(n):
        result += ((- 1) ** i) * (x ** (2*i)) / factorial(2 * i)
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2*i + 1)) / factorial(2*i + 1)
    return result


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2*i)) / factorial(2*i)
    return result


if __name__ == "__main__":
    print(approx_sin(3.14, 10))
    print(approx_cos(3.14, 10))
    print(approx_sinh(3.14, 10))
    print(approx_cosh(3.14, 10))
