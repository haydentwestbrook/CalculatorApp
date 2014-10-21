from calculator.operators import absolute_value


def pythagorean(a, b, mode="h"):
    if mode == "h":
        return (a ** 2 + b ** 2) ** (1 / 2)
    elif mode == "s":
        return (b ** 2 - a ** 2) ** (1 / 2)


def distance(x, y):
    return absolute_value(pythagorean((x[1] - x[0]), (y[1] - y[0])))