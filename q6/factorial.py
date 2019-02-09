import math


def num_of_bintrees(n):
    """
    Make the number of trees for a given node
    :param n: Int
    :return: Int
    """
    fac_ans = math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
    return fac_ans

