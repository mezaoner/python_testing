from functools import wraps

def outer():
    number = 5

    def inner():
        print(number)

    inner()


def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


# print(apply(add, 5, 5))
# print(apply(sub, 5, 5))

def close():
    x = 5
    def inner():
        print(x)
    return inner


# closure = close()
# closure()

def add_to_five(num):
    def inner():
        print(num+5)
    return inner


def log_me(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug("called {} with args {} and kwargs {}".format(
            func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return inner

@log_me
def sub(x,y):
    """returns shit"""
# fifteen = add_to_five(10)
# fifteen()
