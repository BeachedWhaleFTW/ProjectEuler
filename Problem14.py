# Problem 14: Longest Collatz sequence under 1,000,000
# real slow, but future update will use known values of previously calculated numbers for improvement

import time

start = time.time()

def find_collatz(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
            n = int(n)
            count += 1
        else:
            n = int(3*n + 1)
            count += 1
    return count

def find_longest(n):
    longest_length = 0
    number = 1
    for i in range(1, n):
        length = find_collatz(i)
        if length > longest_length:
            longest_length = length
            number = i
    return length, number

length, number = find_longest(1000000)
elapsed = (time.time() - start)

print("Found %s in %s seconds" % (number, elapsed))
