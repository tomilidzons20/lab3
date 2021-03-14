def ntywyraz(a1, n, q):
    an = a1 * q**(n - 1)
    return an


def suma(a1, q, n):
    if q != 1:
        sn = (a1 * ((1 - q**n) / (1 - q)))
    else:
        sn = a1 * n
    return sn
