"""
Nabil Ahmed
ID: 25364170
Task 1
"""
from is_prime import miller_rabin
from prime_factors import prime_factors


def factors(n):

    list_1 = []
    count = 0
    for i in range(n - 1, 1, -1):
        if count >= 100:
            break
        if miller_rabin(i) is True:   # if the num if prime
            new_list = [i+1]          # ck = pk + 1
            list_1.append(new_list)
            count += 1

    for i in range(len(list_1)):
        prime_factor_list = prime_factors(list_1[i][0])
        for j in range(len(prime_factor_list)):   # finds all the prime factors of the given number
            list_1[i].append(prime_factor_list[j])
    main_list = []

    for i in range(len(list_1)-1, -1, -1):
        main_list.append(list_1[i])

    return main_list

import argparse


def commandLine():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("n1", type=int)
    args = argParser.parse_args()
    n1 = args.n1
    return n1

if __name__ == '__main__':
    # n1 = int(input("Enter N: "))
    n1 = commandLine()

    # n1 = 100000000000 works fine with this string
    print(factors(n1))
    list_return = factors(n1)
    f = open('output factors.txt', 'w')
    for i in range(len(list_return)):
        f.write(str(list_return[i][0]) + "\t")
        for j in range(1, len(list_return[i])):
            if j != (len(list_return[i])-1):
                f.write(str(list_return[i][j]) + " x ")
            else:
                f.write(str(list_return[i][j]))
        f.write("\n")
    f.close()
