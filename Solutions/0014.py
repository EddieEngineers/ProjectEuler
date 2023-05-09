# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1 It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers
# finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

from multiprocessing import Pool


def is_even(n):
    return n % 2 == 0


def collatz_sequence(n):
    sequence = [n]
    current_value = n

    while current_value != 1:
        if is_even(current_value):
            current_value //= 2
        else:
            current_value = (3 * current_value) + 1

        sequence.append(current_value)

    return sequence


def solve(low, high):
    longest_sequence_length = 0
    longest_sequence_number = 0

    for number in range(low, high):
        sequence = collatz_sequence(number)
        length_of_sequence = len(sequence)
        if length_of_sequence > longest_sequence_length:
            longest_sequence_length = length_of_sequence
            longest_sequence_number = number

    return longest_sequence_length, longest_sequence_number


if __name__ == '__main__':
    assert (collatz_sequence(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    pool = Pool(10)
    arguments = [
        (2, 100000),
        (100000, 200000),
        (200000, 300000),
        (300000, 400000),
        (400000, 500000),
        (500000, 600000),
        (600000, 700000),
        (700000, 800000),
        (800000, 900000),
        (900000, 1000000)
    ]

    results = []
    for result in pool.starmap(solve, arguments):
        results.append(result)

    longest_sequence_number = sorted(results, reverse=True)[0][1]
    print(longest_sequence_number)
