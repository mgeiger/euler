from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

if __name__ == "__main__":
    total = 0
    maximum = 2000000
    for number in range(0, maximum, 1):
        if is_prime(number):
            total += number
    print("Sum of primes below {}: {}".format(maximum, total))
