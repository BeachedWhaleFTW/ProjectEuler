# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.

def get_primes_below(number):
    prime_list = [2]
    for value in range(3, number + 1, 2):
        if is_prime(value):
            prime_list.append(value)
    return prime_list

def is_prime(number):
    if number % 2 == 0:
        return False
    p = 3
    while p <= number ** 0.5:
        if number % p == 0:
            return False
        p += 2
    return True

print(sum(get_primes_below(2000000)))

# real slow like, but gets the answer eventually.  Probably need to reduce the number of searches based on numbers that
# can't be primes (evens, multiples of 3, 5, etc.)
