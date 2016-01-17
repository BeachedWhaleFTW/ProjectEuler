# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
from math import ceil

def find_triplet_product(number):
    for val1 in range(1, number + 1):
        a = val1
        for val2 in range(1, number + 1):
            b = val2
            for val3 in range(1, number + 1):
                c = val3
                if (a ** 2 + b ** 2) == c ** 2 and a + b + c == number:
                    return a * b * c


print(find_triplet_product(1000))

# works, just real slow.  Need to reduce time by not checking entire space of numbers
