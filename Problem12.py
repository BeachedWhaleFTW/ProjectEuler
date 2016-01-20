# What is the value of the first triangle number to have over five hundred divisors?
import math

def get_factors(n):
    count = 0
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 2
        if i * i == n:
            count -= 1
    return count

number = 0
for n in range(1, 99999999999999):
    number += n
    if get_factors(number) >= 500:
        break

print(number)

