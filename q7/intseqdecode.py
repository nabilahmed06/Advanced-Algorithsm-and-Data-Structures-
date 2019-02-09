"""
Nabil Ahmed
ID: 25364170
Task 3
"""
from enumerate import tree_with_n_nodes
from enumerate import num_of_bintrees
import argparse

# a = "0100110110110010101110100111010101010101010101011"
def commandLine():
    """
    Passes argument into the command line
    :return:
    """
    argParser = argparse.ArgumentParser()
    argParser.add_argument('an_input_file', type=argparse.FileType('r'))
    args = argParser.parse_args()
    an_input_file = ""
    for line in args.an_input_file.read():
        an_input_file += line.strip()
    return an_input_file

f = commandLine()
a = ""

for items in f:
    a += items


a_list = []

zero = 0
one = 0
start = 0
for i in range(len(a)):
    if a[i] == "0":
        zero += 1
    if a[i] == "1" and zero > 0:
        one += 1
    if a[i] == "1" and zero == 0:
        a_list.append([0, int(a[i], 2)])
        one = 0
        start = i + 1

    if one == zero + 1:
        # a_list.append([zero, a[start:i+1]])
        a_list.append([zero, int(a[start:i + 1], 2)])
        start = i + 1
        zero = 0
        one = 0

# find the item with the greatest number of nodes
max_1 = a_list[0][0]
for items in a_list:
    if items[0] > max_1:
        max_1 = items[0]

# now generate tree with the max node
# from task 2
the_biggest_tree = tree_with_n_nodes(max_1)

sum_1 = 0
sum_list = [1]                # contains the sum of the number of trees of n nodes
for i in range(max_1+1):
    s = num_of_bintrees(i)
    sum_1 += s
    sum_list.append(sum_1)

# find the 2nd item in biggest tree and return the first item
upper_lower = []   # iterates in the tree list around this range
for i in range(len(a_list)):
    p_a_list = a_list[i][0]
    lower_limit = sum_list[p_a_list]
    upper_limit = sum_list[p_a_list+1]
    upper_lower.append([lower_limit, upper_limit])

answer_list = []
for i in range(len(a_list)):
    # search item in tree
    # from the starting index to the end
    if upper_lower[i][0] == upper_lower[i][1]:
        answer_list.append(the_biggest_tree[0][0])

    for j in range(upper_lower[i][0], upper_lower[i][1]):
        if a_list[i][1] == the_biggest_tree[j][1]:
            answer_list.append(the_biggest_tree[j][0])


f = open('output intseqdecode.txt', 'w')
for i in range(len(answer_list)):
    if i != len(answer_list) - 1:
        f.write(str(answer_list[i])+",")
    else:
        f.write(str(answer_list[i]))

f.close()
