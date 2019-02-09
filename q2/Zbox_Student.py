"""
Nabil Ahmed
ID: 25364170
Reference : Dr. Lim Wern Han's Code
Z_algorithm
"""

def z_b_o_x(new_string):
    """
    Performs z algorithm on the string
    :param new_string: String
    :return: z array
    """
    z_a_r_r_a_y = [0] * len(new_string)   # creating the z array
    z_a_r_r_a_y[0] = len(new_string)   # first character is the length
    return z_algorithm(z_a_r_r_a_y, new_string)


def z_algorithm(z_array, new_string):
    """

    :param z_array:
    :param new_string:
    :return:
    """
    # giving box boundary
    right_boundary = 0
    left_boundary = 0
    # looping through the string starting at index 1 until the end of the string
    i = 1
    while i < len(new_string):
        # if outside the z-box, then we need to count
        if i > right_boundary:
            greater_than_right_boundary(i, new_string, z_array, left_boundary, right_boundary)
        # if it is within the box
        # i <= right_boundary
        else:
            within_boundary(i, left_boundary, right_boundary, z_array, new_string)
        i += 1
    return z_array

def greater_than_right_boundary(i, new_string, z_array, left_boundary, right_boundary):
    count = 0
    # i outside of the right boundary and it's len is less than the string
    # and its letter is the same as the prefix
    # count : keeps track of the prefix
    while i + count < len(new_string) and new_string[count] == new_string[i + count]:
        count += 1   # increment count
    z_array[i] = count  # set the z-value at i
    # Zi_suffix box exists update the box boundary
    if count > 0:
        left_boundary = i
        right_boundary = i + count - 1
    return z_array, left_boundary, right_boundary


def within_boundary(i, left_boundary, right_boundary, z_array, new_string):
    # get the paired prefix index (z-value) to copy
    index_prefix = i - left_boundary
    # the remaining length of the box
    remaining = right_boundary - i + 1
    # case 2a
    # if the z-value at prefix is still within the remaining box
    if z_array[index_prefix] < remaining:
        z_array[i] = z_array[index_prefix]  # copy the value
    # case 2b
    # if the value is the exactly the box
    # then we need to extend/ find Zi_suffix new box
    elif z_array[index_prefix] == remaining:
        new_right = right_boundary + 1
        while new_right < len(new_string) and new_string[new_right] == new_string[new_right - i]:
            new_right += 1
        # update the z-array with the extension
        z_array[i] = new_right - i
        # new left_boundary and right_boundary boundary
        left_boundary = i
        right_boundary = new_right - 1
    # case 2c
    # if the value is greater than the remaining (going outside the box)
    # then we know only the remaining of the box is the same as the prefix
    # note this is z_array[index_prefix] > remaining
    else:
        z_array[i] = remaining
    return z_array
