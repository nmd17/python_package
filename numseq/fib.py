from math import sqrt


def fib(n):
    '''will return the nth number in the fibonacci sequence'''

    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
