MAX_FIB = 4000000
total = 0

prior_fib = 1
current_fib = 2

while current_fib < MAX_FIB:
    if not (current_fib % 2):
        total += current_fib
    new_fib = prior_fib + current_fib
    prior_fib = current_fib
    current_fib = new_fib

print(total)
