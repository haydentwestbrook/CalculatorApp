def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def integer_divide(a, b):
    return a // b


def root(base, root):
    return base ** (1/root)


def power(base, power):
    return base ** power


def absolute_value(n):
    if n < 0:
        return n * -1
    else:
        return n