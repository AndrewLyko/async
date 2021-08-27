import inspect


def gen():
    yield 2
    yield 3


g = gen()
print(inspect.getgeneratorstate(g))
