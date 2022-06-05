# format of formatting:-
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
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
