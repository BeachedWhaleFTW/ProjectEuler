# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?

number = 600851475143
test = 2000000

def find_largest_prime_factor(number):
    i = 2
    while i * i < number:
        while number % i == 0:
            number /= i
        i += 1
    return int(number)

print(find_largest_prime_factor(number))