def my_gcd(m,n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n