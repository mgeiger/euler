def is_palindrome(val):
    return str(val) == str(val)[::-1]

for i in range(1000, 99, -1):
    sq = i * i
    if is_palindrome(sq):
        print('Value: {}'.format(i))
        print('Square: {}'.format(sq))
        break
