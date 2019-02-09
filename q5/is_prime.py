import random


def miller_rabin(n):
    """
    Returns True if num is a prime number.
    :param n: Int
    :return: Bool
    """
    assert n > 1, "Enter a positive integer greater than or equal to 2"
    if n == 2 or n == 3:
        return True
    
    if n % 2 == 0:
        return False

    before = n - 1
    k_1 = 0
    while before % 2 == 0:
        before //= 2
        k_1 += 1

    for item in range(100):
        a = random.randrange(2, n - 1)
        to_the_pow = pow(a, before, n)
        if to_the_pow != 1:
            i = 0
            while to_the_pow != (n - 1):
                if i == k_1 - 1:
                    return False
                else:
                    i += 1
                    to_the_pow = (to_the_pow ** 2) % n
    return True
