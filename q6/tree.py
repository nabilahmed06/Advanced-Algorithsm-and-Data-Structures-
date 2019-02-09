

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
