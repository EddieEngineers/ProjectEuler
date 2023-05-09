# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
from math import sqrt


def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solve():
    prime_numbers = []
    i = 0

    while len(prime_numbers) < 10001:
        if is_prime(i):
            prime_numbers.append(i)

        i += 1

    return prime_numbers[-1]


if __name__ == '__main__':
    print(solve())
