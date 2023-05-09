# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math


def sum_pythagorean_triple(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return a + b + c


def solve():
    for a in range(1, 500):
        for b in range(a + 1, 500):
            if sum_pythagorean_triple(a, b) == 1000:
                return a * b * math.sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    print(int(solve()))
