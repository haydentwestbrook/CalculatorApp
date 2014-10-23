def ln(value, n=500):
    #Returns an approximation of the
    #natural log of the value out to
    #n terms. n = 500 by default.
    if value == 0:
        return None
    if value < 0:
        raise TypeError()
    sum = 0.0
    if value < 1:
        for i in range(1, n + 1):
            sum += (((-1.0) ** (i + 1.0)) * ((value - 1.0) ** i)) / i
    else:
        for i in range(1, n + 1):
            sum += 1 / (i * (value / (value - 1)) ** i)
    return sum


def log(value, base=10, n=500):
    #Returns an approximation of the
    #log of the value utilizing a base
    #change from the natural log out to
    #n terms. n = 500 by default.
    return ln(value, n) / ln(base, n)