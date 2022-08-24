"""
this progra
"""


def isprime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, (n//2+1)):
            if n % i == 0:
                return False
        return True


print(isprime(1))
print(isprime(2))
print(isprime(10))
print(isprime(11))
print(isprime(12))
print(isprime(13))
