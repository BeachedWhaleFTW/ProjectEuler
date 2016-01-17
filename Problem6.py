# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 − 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

def square_of_sums(n):
    sum = 0
    for number in range(1, n):
        sum += number
    return sum * sum

def sum_of_squares(n):
    square_sum = 0
    for number in range(1, n):
        square_sum += (number * number)
    return square_sum

n = 101

print(sum_of_squares(n), square_of_sums(n), (square_of_sums(n) - sum_of_squares(n)))
