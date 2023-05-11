# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def is_prime(x):
  if x == 2:
    return True

  i = 2
  while i < x:
    if x % i == 0:
      return False
    i += 1

  return True


def solve(n):
  answer = 0
  for x in range(2, n):
    if is_prime(x):
      answer += x

  return answer


if __name__ == '__main__':
  print(solve(2000000))
