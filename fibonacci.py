"""Uncomment the functions you want to learn"""
""
"""def fib(n):
    a, b = 0, 1
    print(a, end=',')
    print(b, end=',')
    for i in range(n):
        fibs = a+b
        a, b = b, fibs
        print(fibs, end=',')


fib(10)"""
"""alternate way
    Print all numbers in fibonacci series less than n"""

"""a, b = 0, 1
print(0)
while b < 100:
    print(b)
    a, b = b, a+b"""

"""Print all numbers in fibonacci series less than n(list and loops)"""


def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


print(fib(100))
