"""
this program showcases random number gene
"""
import random
"""for random number"""
# [0.0, 1.0)
print(random.random())
"""for random number from 0(automatically taken) to 10(here)"""
print(random.randrange(10))
"""for random number from 1(here) to 10(here)"""
print(random.randrange(1, 10))
"""for random number from 1(here) to 10(here), only odd"""
print(random.randrange(1, 10, 2))
"""a <= n <= b(i.e, includes b too, unlike randrange)"""
print(random.randint(20, 30))
"""picks a random number from a group of values"""
print(random.choice([1, 2, 3, 4]))
"""picks a random number from a group of string"""
print(random.choice("Hello"))
"""picks a random number from a group of values from tupples"""
print(random.choice((10, 20, 30, 40, 50, 60)))
"""make a function to generate nums"""


def rangen(a, b):
    return random.randrange(a, b)


print(rangen(10, 20))
print(rangen(20, 30))
print(rangen(30, 40))
