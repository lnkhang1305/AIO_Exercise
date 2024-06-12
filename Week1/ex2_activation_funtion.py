import math


def is_number(number):
    try:
        float(number)
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return int(x <= 0) * 0 + int(x > 0) * x


def elu(x, a=0.01):
    return int(x <= 0) * a * (math.exp(x) - 1) + int(x > 0) * x


x = input('Input x: ')
if is_number(x):
    activation_func = input(
        'Input activation Function (sigmoid | relu | elu): ')
    if activation_func not in {'sigmoid', 'relu', 'elu'}:
        print(activation_func, ' is not supported')
    else:
        x = float(x)
        if activation_func == 'sigmoid':
            print(sigmoid(x))
        if activation_func == 'relu':
            print(relu(x))
        if activation_func == 'elu':
            print(elu(x))
else:
    print('x must be a number')
