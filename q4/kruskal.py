"""
Kruskals Algorithm
Minimum Spanning Tree
Nabil Ahmed
ID: 25364170
"""

from mergesort import merge_sort
import argparse


def read_from_cmd():
    """
    This function takes input from the command line and then inserts the contents of the file to strings.
    :return:
    """
    a_variable = argparse.ArgumentParser()
    a_variable.add_argument('inputgraphfile', type=argparse.FileType('r'))
    args = a_variable.parse_args()
    graph = []
    for item in args.inputgraphfile.readlines():
        graph.append(item.split())
    return graph

file = read_from_cmd()

def converted_List(List_1):
    """
    Converts the string to Integers
    :param List_1:
    :return: List
    """
    for items in List_1:
        tmp = items[0]
        tmp1 = items[1]
        tmp2 = items[2]
        items[0] = int(tmp)
        items[1] = int(tmp1)
        items[2] = int(tmp2)
    return List_1

a_List = converted_List(file)

Vertices_List = []
for items in a_List:     # Listing all the vertices
    Vertices_List.append(items[0])
    Vertices_List.append(items[1])

vertices = []             # Contains all the unique vertex
for item in Vertices_List:
    if item not in vertices:
        vertices.append(item)

parent_array = []         # initializing the disjoints set
for i in range(len(vertices)+1):
    parent_array.append(-1)

sorted_edges = merge_sort(a_List)  #sorted_edges contains the sorted list by weight


def find(a):
    if parent_array[a] < 0:   # find root of the tree containing ‘a’
        return a
    parent_array[a] = find(parent_array[a])
    return parent_array[a]


def union(a,b):  # by height
    root_a = find(a)   # find root of tree containing ‘a’
    root_b = find(b)   # find root of tree containing ‘b’
    if root_a == root_b:  # ‘a’ and ‘b’ in the same tree
        return
    height_a = -parent_array[root_a]  # height of tree containing ‘a’
    height_b = -parent_array[root_b]  # height of tree containing ‘b’
    if height_a > height_b:
        parent_array[root_b] = root_a # link shorter tree’s root to taller
    elif height_b > height_a:
        parent_array[root_a] = root_b

    else:                             # update height
        parent_array[root_a] = root_b
        parent_array[root_b] = -(height_b + 1)

Finalized_List = []

for z in range(len(sorted_edges)):
    if len(Finalized_List) >= len(parent_array) -1:     # Minimum spanning tree already formed
        break
    if find(sorted_edges[z][0]) != find(sorted_edges[z][1]): # if u and v not in the same class
        Finalized_List.append(sorted_edges[z])               # add
        union(sorted_edges[z][0],sorted_edges[z][1])         # then merge

# output to a .txt file
f = open('output_kruskal.txt', 'w')
for v1, v2, w in Finalized_List:
    f.write('{:>0} {:>1} {:>1} \n'.format(v1, v2, w))
f.close()
