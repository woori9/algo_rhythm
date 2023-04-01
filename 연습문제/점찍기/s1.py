import math


def solution(k, d):
    x = y = 0
    result = 0
    d_square = d ** 2

    while y <= d:
        result += math.floor((d_square - y ** 2) ** (1 / 2)) // k + 1
        y += k

    return result
