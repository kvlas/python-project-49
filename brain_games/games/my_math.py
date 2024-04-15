def is_even(a):
    if (a % 2) == 0:
        return True
    else:
        return False


def my_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b


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
