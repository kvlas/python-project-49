def my_gcd(m,n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n


def my_ap(a, d, n):
    curr_term = a
    lst = []
    for i in range(1, n + 1):
        curr_term = curr_term + d
        lst.append(curr_term)
    return lst

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True