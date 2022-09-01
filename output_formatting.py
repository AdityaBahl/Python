"""
this program sh
"""
# format of formatting:-
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
import sys
from math import pi
import math
print(1, 2, 3, 4, sep='#', end='&\n')

# output formatting
x = 5
y = 10
print('The value of x is {} and y is {}'.format(x, y))

# another way, sequencing by 0 and 1
print('I love {0} and {1}'.format('bread', 'butter'))
print('I love {1} and {0}'.format('bread', 'butter'))

# We can even use keyword arguments to format the string
print('Hello {name}, {greeting}'.format(greeting='Goodmorning', name='John'))

# floating precision point
a = 12.3456789
print('The value of a is %3.2f' % a)
print('The value of a is %3.4f' % a)

# input
num = input('Enter a number: ')
print(num)

# typecasting
print(int('10'))
print(float('10'))
# int('2+3')doesnt work
print(int('2'+'3'))  # concatinates like a string instead do,
print(eval('2+3'))

# python import
# When our program grows bigger, it is a good idea to break it into different modules.
# A module is a file containing Python definitions and statements. Python modules have a filename and end with the extension .py.
# Definitions inside a module can be imported to another module or the interactive interpreter in Python. We use the import keyword to do this.
# For example, we can import the math module by typing the following line:
print(math.pi)  # imported from line 5
print(pi)  # alternate way of importing, line 4


# While importing a module, Python looks at several places defined in sys.path. It is a list of directory locations.
sys.path  # from line 3
