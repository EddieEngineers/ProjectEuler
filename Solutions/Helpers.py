from math import ceil, sqrt


def is_prime(x):
  if x == 2:
    return True

  i = 2
  while i < x:
    if x % i == 0:
      return False
    i += 1

  return True


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


def fib(limit):
  if limit == 1:
    return [1]

  if limit == 2:
    return [1, 1]

  fib_sequence = [1, 1]

  while fib_sequence[-1] + fib_sequence[-2] < limit:
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

  return fib_sequence
