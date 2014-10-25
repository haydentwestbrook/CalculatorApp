from operators import absolute_value
from operators import power
from operators import add
from operators import subtract


def pythagorean(a, b, mode="h"):

    c = 0

    if mode == "h":
        c = power(add(power(a,2),power(b,2)),.5)
        #c = ((a ** 2 + b ** 2) ** (1 / 2))
    else:
        c = power(absolute_value(subtract(power(b,2),power(a,2))),.5)
        #c = ((b ** 2 - a ** 2) ** (1 / 2))

    return c


def distance(x1, y1, x2, y2):
    return absolute_value(pythagorean((x1 - x2), (y1 - y2)))


def fib(x):
    # Takes a variable x and will find that number in the Fibonacci Sequence
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def continuous_fib(x):
    for i in range(x+1):
        print(fib(i))
    return fib(x)