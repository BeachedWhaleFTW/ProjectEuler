# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(number):
    if number % 2 == 0:
        return False
    p = 3
    while p <= number ** 0.5:
        if number % p == 0:
            return False
        p += 2
    return True

def find_nth_prime(n):
    prime_number = 2
    no_prime = 1
    number = 3
    while no_prime < n:
        if is_prime(number):
            prime_number = number
            no_prime += 1
        number += 2
    return prime_number

n = 10001
print(find_nth_prime(10001))