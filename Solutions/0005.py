# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_divisible(number, divisors):
    for divisor in divisors:
        if number % divisor != 0:
            return False

    return True


def solve():
    number = 20
    while True:
        if is_divisible(number, list(range(1, 21))):
            return number
        else:
            number += 20


if __name__ == '__main__':
    print(solve())
