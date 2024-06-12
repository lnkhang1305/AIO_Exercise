import math
import random


def mae(n, predict, target):
    result = 0
    for i in range(n):
        print(f"loss name: MAE, sample: {i + 1}, pred: {predict[i]}, target: {target[i]},")
        result += abs((predict[i] - target[i]))
        print(f'loss: {result}')
    return result/n


def mse(n, predict, target):
    result = 0
    for i in range(n):
        print(f'loss name: mse, sample: {i + 1}, pred: {predict[i]}, target: {target[i]},')
        result += (predict[i]-target[i]) ** 2
        print(f'loss: {result}')
    return result / n


def rmse(n, predict, target):
    result = 0
    for i in range(n):
        print(f'loss name: rmse, sample: {i + 1}, pred: {predict[i]}, target: {target[i]},')
        result += math.sqrt((predict[i]-target[i]) ** 2)
        print(f'loss: {result}')
    return result / n


if __name__ == "__main__":
    num_samples = input('Input number of samples: ')
    if num_samples.isnumeric():

        num_samples = int(num_samples)

        predict = [random.uniform(0, 10) for _ in range(num_samples)]
        target = [random.uniform(0, 10) for _ in range(num_samples)]

        loss_func = input('Input loss function: ')
        if loss_func == 'mae':
            print(mae(num_samples, predict, target))
        elif loss_func == 'mse':
            print(mse(num_samples, predict, target))
        else:
            print(rmse(num_samples, predict, target))
    else:
        print('Number of samples must be int')