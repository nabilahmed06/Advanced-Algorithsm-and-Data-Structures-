"""
Nabil Ahmed
ID: 25364170
Task 2
The following program generates the tree that is the
bitstring associated with its pre-order traversal
"""
from factorial import num_of_bintrees
from tree import enumerate_tree_for_n_value


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
    final_list = []
    for i in range(len(main_list)):
        final_list.append([i+1, main_list[i]])

    return final_list

import argparse

def commandLine():
    """
    Passes argument into the command line
    :return:
    """
    argParser = argparse.ArgumentParser()
    argParser.add_argument("abc", type=int)
    args = argParser.parse_args()
    abc = args.abc
    return abc

if __name__ == "__main__":
    abc = commandLine()
    a_tree = tree_with_n_nodes(abc)
    # print(a_tree)
    f = open('output enumerate.txt', 'w')

    for i in range(len(a_tree)):
        f.write(str(a_tree[i][0]) + "\t" + str(a_tree[i][1]))

        f.write("\n")
    f.close()
