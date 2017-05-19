""""
docstring
"""


def fib(n):
    a, b, c = 0, 1, 0
    while a < n:
        # print(a, end=' ')
        a, b = b, a + b
        c = c + 1
        print("a:", a, "b:", b, "c:", c)
    print()


fib(1000)
