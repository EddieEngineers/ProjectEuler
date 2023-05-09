# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
from math import ceil
from multiprocessing import Pool


def is_prime(x):
    if x == 2:
        return True

    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1

    return True


def solve(low, high):
    answer = 0
    for x in range(low, high):
        if is_prime(x):
            answer += x

    return answer


if __name__ == '__main__':
    target = 2000000
    answer = 0

    quarter = ceil(target * 0.25)
    half = ceil(target * 0.5)
    third_quarter = ceil(target * 0.75)

    arguments = [(2, quarter), (quarter, half), (half, third_quarter), (third_quarter, target)]

    pool = Pool(4)
    for result in pool.starmap(solve, arguments):
        answer += result

    print(answer)
