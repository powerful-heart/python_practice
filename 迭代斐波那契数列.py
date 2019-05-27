"""
迭代实现斐波那契数列
"""


def fib(n):
    a, b = 1, 1

    while n > 0:
        print(a, end=' ')
        a, b = b, a + b
        n -= 1
    print()


fib(5)
