# Problem 15: 20 x 20 route problem

import time, math

start = time.time()

# (40!/20!)/20! - Combination of having 20 x 20 routes

def get_routes(n):
    return int((math.factorial(n*2)/math.factorial(n))/math.factorial(n))

number = get_routes(20)

elapsed = (time.time() - start)

print("Found %s in %s seconds" % (number, elapsed))