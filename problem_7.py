primes = [2, 3, 5, 7, 11, 13]

current_eval = primes[-1]

while len(primes) <= 10001:

    current_eval += 1

    found_divisor = False
    
    for prime in primes:
        if not (current_eval % prime):
            found_divisor = True
        if found_divisor:
            break

    if not found_divisor:
        primes.append(current_eval)

print('Found {} prime numbers'.format(len(primes)))
print(primes[-2])
