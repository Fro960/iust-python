import math

def get_factors(n):
    factors = set()
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors

print(get_factors(20))