import math


def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))

n = 9
print(fibonacci(n))
