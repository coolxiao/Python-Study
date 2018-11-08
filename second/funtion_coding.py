from functools import reduce

a = abs
print(a(-1))


# map
def f(x):
    return x * x


b = list(range(10))
c = map(f, b)
print(list(c))


# reduce
def add(x, y):
    return x + y


d = reduce(add, list(range(10)))
print(d)

e = lambda x: x * x
print(e(10))


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2018-11-08')


now()
