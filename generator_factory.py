def pipeline(number):
    data = (i for i in range(number))
    squared = (i ** 2 for i in data)
    negated = (-i for i in squared)
    return (n + 1 for n in negated)


# generator factory

## paczka itertools import *

pipe = pipeline(10)
print(next(pipe))
print(next(pipe))
print(next(pipe))
print(next(pipe))

from itertools import accumulate

print(list(accumulate([1, 2, 3, 4, 5])))
