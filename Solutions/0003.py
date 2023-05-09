# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
from math import ceil, sqrt


def factorize(n):
    prime_numbers = []

    n = n

    for i in range(2, ceil(sqrt(n))):
        while n % i == 0:
            prime_numbers.append(i)
            n = n / i

    if n > 2:
        prime_numbers.append(n)

    return prime_numbers


def solve(n):
    prime_factors = factorize(n)
    return prime_factors[-1]


if __name__ == '__main__':
    print(solve(600851475143))
