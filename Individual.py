# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(x, n):
    if n == 0:
        a = 1

    elif n < 0:
        a = 1 / f(x, abs(n))

    else:
        a = x * (pow(x, (n-1)))

    return a


if __name__ == '__main__':
    print("Введите x:")
    x = float(input())
    print("Введите n:")
    n = int(input())
    print("Результат рекурсивной функции: ", f(x, n))