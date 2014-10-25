from operators import absolute_value


def pythagorean(a, b, mode="h"):
    if mode == "h":
        return (a ** 2 + b ** 2) ** (1 / 2)
    else:
        return (b ** 2 - a ** 2) ** (1 / 2)


def distance(x, y, w, z):
    return absolute_value(pythagorean((x - w), (y - z)))


def fib(x):
    # Takes a variable x and will find that number in the Fibonacci Sequence
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def continues_fib(x):
    for i in range(x+1):
        print(fib(i))
    return fib(x)