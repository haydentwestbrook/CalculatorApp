from operators import factorial


def sin(angle, n=75):
    #Returns the sine approximation for the
    #angle out to n terms. n = 75 by default
    sum = 0.0
    for i in range(n + 1):
        sum += (((-1.0) ** i) * (angle ** (2.0 * i + 1.0))) / factorial(2 * i + 1)
    return sum


def cos(angle, n=75):
    #Returns the cosine approximation for the
    #angle out to n terms. n = 75 by default
    sum = 0.0
    for i in range(n + 1):
        sum += (((-1.0) ** i) * (angle ** (2.0 * i))) / factorial(2 * i)
    return sum


def tan(angle, n=75):
    #Returns the tangent approximation for the
    #angle out to n terms. n = 75 by default
    return sin(angle, n) / cos(angle, n)


def sec(angle, n=75):
    #Returns the secant approximation for the
    #angle out to n terms. n = 75 by default
    return 1.0 / cos(angle, n)


def csc(angle, n=75):
    #Returns the cosecant approximation for the
    #angle out to n terms. n = 75 by default
    return 1.0 / sin(angle, n)


def cot(angle, n=75):
    #Returns the cotangent approximation for the
    #angle out to n terms. n = 75 by default
    return 1.0 / tan(angle, n)