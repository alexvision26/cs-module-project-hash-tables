# Your code here
import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

lookup = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    v = (x,y)
    if v not in lookup:
        lookup[v] = slowfun_too_slow(x,y)

    return lookup[v]




# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')




# trade space for time

# lookup_table = {}

# def inverse_root(n):
#     return 1 / math.sqrt(n)

# def build_lookup_table():

#     for i in range(1, 1000):
#         lookup_table[i] = inverse_root(i)

# build_lookup_table()

# print(lookup_table[556])
# print(lookup_table[99])
# print(lookup_table[999])