# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
import math

def check_product(number):
    for product in range(999, 99, -1):
        remainder = 0
        if number % product == 0:
            remainder = number/product
            remainder = int(remainder)
        if len(str(remainder)) == 3:
            print(product, remainder)
            return True
    return False

for number in range(999 * 999, 100 * 100, -1):
    str_number = str(number)
    n = 0
    for index in range(len(str_number)):
        if str_number[-(index + 1)] == str_number[index]:
            n += 1
    if n == len(str_number) and check_product(number):
        print(number)
        break





