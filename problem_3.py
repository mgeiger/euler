from math import sqrt
from itertools import count, islice

def is_prime(a):
    return a > 1 and all(a%i for i in islice(count(2), int(sqrt(a) - 1)))

def largest_prime_factor(eval_num):
    top_number = None

    check_num = 2
    largest_eval = int(sqrt(eval_num))
    while check_num < largest_eval:

        if not(eval_num % check_num):
            # This means we have a divisible number

            if is_prime(eval_num / check_num):
                return eval_num / check_num
            elif is_prime(check_num):
                top_number = check_num

        check_num += 1

    return top_number


check_numbers = [9, 29, 13195, 600851475143, 600851475143]

for check_number in check_numbers:
    print(is_prime(check_number))
    print(largest_prime_factor(check_number))
