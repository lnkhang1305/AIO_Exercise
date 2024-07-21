import numpy as np
import cv2 as cv


def compute_difference(bg, input):
    diff = input - bg
    return diff


def compute_binary_mask(diff):
    rs = np.where(diff > 0, 255, 0)
    return rs


def replace_background(bg1, bg2, ob):
    diff = compute_difference(ob, bg1)
    binary_mask = compute_binary_mask(diff)

    result = np.where(binary_mask == 255, ob, bg2)
    return result


if __name__ == '__main__':
    bg1 = cv.imread(
        r'C:\Users\Acer\OneDrive - VNU-HCMUS\AIO2024\AIO_Exercise\Week6\image\GreenBackground.png', 1)
    bg1 = cv.resize(bg1, (678, 381))

    ob = cv.imread(
        r'C:\Users\Acer\OneDrive - VNU-HCMUS\AIO2024\AIO_Exercise\Week6\image\Object.png', 1)
    ob = cv.resize(ob, (678, 381))

    bg2 = cv.imread(
        r'C:\Users\Acer\OneDrive - VNU-HCMUS\AIO2024\AIO_Exercise\Week6\image\NewBackground.jpg', 1)
    bg2 = cv.resize(bg2, (678, 381))

    result = replace_background(bg1, bg2, ob)
    cv.imshow('bg1', bg1)
    cv.imshow('ob', ob)
    cv.imshow('bg2', bg2)
    cv.imshow('result', result)
    cv.waitKey(0)
