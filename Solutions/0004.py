# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(value):
    palindrome = int(''.join([d for d in str(value)])[::-1])
    return value == palindrome


def solve():
    a = 100
    b = 100
    largest_palindrome = 0

    while a < 1000:
        while b < 1000:
            print(f'{a} * {b}')
            product = a * b
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

            b += 1
        a += 1
        b = 100

    return largest_palindrome


if __name__ == '__main__':
    print(is_palindrome(100001))
    print(solve())
