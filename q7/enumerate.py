"""
Nabil Ahmed
ID: 25364170
Task 2
The following program generates the tree that is the
bitstring associated with its pre-order traversal
"""
import math


def num_of_bintrees(n):
    fac_ans = math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
    return fac_ans


def enumerate_tree_for_n_value(a):
    """
    This functions takes a list/list of list
    and does pre order traversal and generates the bit string
    :param a: List/List of List
    :return: A list containing the valid substring
    """
    b = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == "1":
                b.append(a[i][:j] + "01" + a[i][j:])

    c = []
    max_1 = int(b[0], 2)
    c.append(b[0])
    for i in range(1, len(b)):
        if int(b[i], 2) > max_1:
            c.append(b[i])
            max_1 = int(b[i], 2)

    return c


def tree_with_n_nodes(n):
    """
    Makes a tree with N internal nodes that traverses in the pre-order sequence generating it's bitstring
    :param n: Int
    :return: A List
    """
    main_list = []

    n1 = 0
    while n1 <= n:
        if n1 == 0:
            main_list.append("1")

        if n1 == 1:
            main_list.append("011")

        if n1 >= 2:
            total_trees_prev_node = num_of_bintrees(n1 - 1)
            previous = len(main_list) - total_trees_prev_node
            editing_list = []
            for i in range(previous, len(main_list)):
                editing_list.append(main_list[i])
            # print("editing: " + str(editing_list))
            a_list = enumerate_tree_for_n_value(editing_list)
            for i in range(len(a_list)):
                main_list.append(a_list[i])

        n1 += 1

    numbers_list = []
    for i in range(len(main_list)):
        numbers_list.append([i+1])

    for i in range(len(main_list)):
        numbers_list[i].append(int(main_list[i], 2))

    return numbers_list

if __name__ == "__main__":
    abc = int(input("Enter N: "))
    print(tree_with_n_nodes(abc))
