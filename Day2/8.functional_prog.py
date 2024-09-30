import math

def add(x):
    return x + 2

def square(x):
    return math.sqrt(x)

print(add(2))

l = (1, 1, 1, 2, 9, 64)
print(list(map(square, l)))



def greater(x):
    return x > 1

print(list(filter(greater, l)))

from functools import reduce

l = (1, 1, 1, 2, 9, 64)
def add_two_no(x, y):
    return x + y

print(reduce(add_two_no, l))


from functools import reduce
l = [3, 5, 10, 4, 50, 11, 20]
print(reduce(lambda x, y: x if x >y else y , l))
