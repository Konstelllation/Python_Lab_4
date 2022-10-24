# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x, n):
    if n == 0:
        return 1
    if n == -1:
        return 1. / x
    p = f(x, n // 2)
    p *= p
    if n % 2:
        p *= x
    return p



if __name__ == '__main__':
    print("Введите x:")
    x = float(input())
    print("Введите n:")
    n = int(input())
    print("Результат рекурсивной функции: ", f(x, n))