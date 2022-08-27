"""
this pro
"""


def greet(name):
    print('Hello', name, '! How Are You?')


def greet1(name, message):
    print('Hello', name, message)


greet1('Aditya', '! Wassup?')
greet('Nandika')
greet('Shipra')
greet1('Priya', 'Lesgooo')
greet('Aryan')


def sums(a, b):
    return a+b


print(sums(10, 20))
print(sums(30, 20))
print(sums(10, 60))
print('aditya', 'bahl')
print(10+20)


def returnmultiplevalues():
    a, b, c = 1, 2, 3
    return a, b, c


x, y, z = returnmultiplevalues()
print(x, y, z)


def multiply(a=2, b=3):
    return a*b


print(multiply(4, 5))
print(multiply(5,))
