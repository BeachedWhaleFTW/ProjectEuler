# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
num_range = range(1, 21)

def divisible_by_all(step):
    for num in range(2520, 999999999999999, step):
        if all(num % n == 0 for n in num_range):
            return num
    return None

print(divisible_by_all(2520))

