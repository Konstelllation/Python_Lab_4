import math

def f (x, n):
    if n == 0:
        x = 1
        return(x)

    elif n < 0:
        x = 1 / x ** (abs(n))
        return(x)

    else:
        x = x * (x ** (n-1))
        return(x)

if __name__ == '__main__':
    print("Введите x:")
    x = float(input())
    print ("Введите n:")
    n = int(input())
    print("Результат рекурсивной функции: ", f(x,n))