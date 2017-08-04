MAX_NUMBER = 1000

total = 0
for num in range(0, 1000):
    if not (num % 3) or not (num % 5):
        total += num
print(total)
