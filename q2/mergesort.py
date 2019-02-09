"""
Nabil Ahmed
ID: 25364170
Reference mergesort
http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
"""


def merge_sort(a_list):
    """
    Algorithm Performs a MergeSort On a list of elements
    :param a_list:
    :return:
    """
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_side = a_list[:mid]
        right_side = a_list[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        i = 0
        j = 0
        k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i][0] < right_side[j][0]:
                a_list[k] = left_side[i]
                i += 1
            else:
                a_list[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            a_list[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            a_list[k] = right_side[j]
            j += 1
            k += 1
    # return a_list


alist = [[6, 1], [9, 0], [0, 1], [9, 0]]
# For testing purposes
# print(mergeSort(alist))
