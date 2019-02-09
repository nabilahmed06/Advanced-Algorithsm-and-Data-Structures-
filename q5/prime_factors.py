import math


def prime_factors(n_1):
    """
    returns prime factors
    :param n_1: int
    :return: a list
    """
    list_1 = []
    while n_1 % 2 == 0:  # append 2 as long as it is a factor
        list_1.append(2)
        n_1 /= 2

    for i in range(3, int(math.sqrt(n_1)) + 1, 2): # iterate until sqrt to find if it is prime or not
        while n_1 % i == 0:
            list_1.append(int(i))
            n_1 /= i

    if n_1 > 2:
        list_1.append(int(n_1))

    return list_1

