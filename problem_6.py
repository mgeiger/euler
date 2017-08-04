sq_sum = sum(range(1, 101, 1))**2
sum_sq = sum([x**2 for x in range(1, 101, 1)])

print('Sqaure of Sums: {}'.format(sq_sum))
print('Sum of Squares: {}'.format(sum_sq))

print('Difference: {}'.format(abs(sq_sum - sum_sq)))
