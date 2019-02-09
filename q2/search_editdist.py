"""
Q2
Nabil Ahmed
ID: 25364170
Edit Distance
"""

from mergesort import merge_sort
from Boyer_Moore import BoyerMoore

def odd_or_even_length(pat_1):
    """
    Splits the length into 2 segments depending on the length of the string
    :param pat_1: <String>
    :return: 2 strings
    """
    if len(pat_1) % 2 == 0:  # even
        first_half = pat_1[:len(pat_1) // 2]
        second_half = pat_1[len(pat_1) // 2:len(pat_1)]
    else:  # odd
        first_half = pat_1[:len(pat_1) // 2]
        second_half = pat_1[len(pat_1) // 2:len(pat_1)]
    return first_half, second_half


def edit_dist():
    """
    This function will find all the edits <= 1 in the text
    This function employs an algorithm that took it's inspiration from the
    pigeon hole principal. It splits the pattern into 2 parts.
    Our Aim is to find the edit distance <= 1 in text
    Meaning one part of the pattern will be an exact match
    We find this match using the boyer moore algorithm
    So, for the first part of the pat the boyer moore algorithm
    finds all the occurrences of PAT in TEXT.
    We, then access the TEXT in those specific areas and then compare
    the 2nd part of the pattern one letter at a time
    using the insertion, deletion and substitution principal.
    As, soon as the edits are more than 1 we break the iteration.
    The substitution principal is simple, as soon as the letter in the
    TEXT and PAT is a mismatch it is under substitution.
    So, we increase the count value by 1.
    So, we then check diagonally. This diagonal checking ensures
    the insertion and deletion principal.
    Lets say, at some iteration where k-index is iterating through the
    TEXT and j-index is iterating through the PAT.
    There occurs a mismatch. i.e TEXT[k] != PAT[j]:
    We then check the diagonals. i.e.
        if TEXT[k+1] == PAT[j]:
            we increment the k and the comparison goes as TEXT[k+1....] with PAT[j.....]
            in PAT and TEXT
        if TEXT[k] == PAT[j+1]:
            we increment the j and the comparison goes as TEXT[k....] with PAT[j+1.....]
            in PAT and TEXT
    :return: edit_dist list with <= 1 edits
    """

    split_word = odd_or_even_length(pat)
    first_part = split_word[0]    # 1st part of the pat
    second_part = split_word[1]   # 2nd part of the pat
    edit_dist_list = []           # List that will contain all the edits <= 1

    # Starting the first part
    first_part_boyer_moore = BoyerMoore(text, first_part)
    # if there are occurces i.e. exact matches of PAT in TEXT
    # only then do:
    if len(first_part_boyer_moore) > 0:
        # Remove the last element from the list if its len of 2nd part of PAT goes out of TEXT
        # This basically the check the last index so the list does not go out of range while
        # the program is being run
        if first_part_boyer_moore[-1] + len(pat) > len(text):
            first_part_boyer_moore.remove(first_part_boyer_moore[-1])

        i = 0
        while i < len(first_part_boyer_moore):
            # pigeon hole principal applied here
            # described earlier in the function top
            counter = 0
            j = 0
            k = 0
            while j < len(second_part)-1 and k < len(second_part)+1:
                if counter >= 2:
                    # more than 1 edit
                    break
                if text[first_part_boyer_moore[i] + len(first_part) + k] != pat[len(first_part) + j]:  # mismatch
                    counter += 1
                    # Diagonal Checking
                    if text[first_part_boyer_moore[i] + len(first_part) + k + 1] == pat[len(first_part) + j]:
                        j -= 1
                    if text[first_part_boyer_moore[i] + len(first_part) + k] == pat[len(first_part) + j + 1]:
                        k -= 1

                k += 1
                j += 1
            if counter <= 1:
                # appending the index of the PAT in TEXT with less than one edit
                edit_dist_list.append([first_part_boyer_moore[i], counter])
            i += 1
    # Starting the 2nd part
    second_part_boyer_moore = BoyerMoore(text, second_part)
    if len(second_part_boyer_moore) > 0:
        # checking the first element to see if it will get out of index while
        # the program is being run
        if second_part_boyer_moore[0] - len(first_part) < 0:
            second_part_boyer_moore.remove(second_part_boyer_moore[0])

        i = 0
        while i < len(second_part_boyer_moore):
            # pigeon hole principal applied
            counter = 0
            k = len(first_part) - 1
            j = len(first_part) - 1
            while j > 0 and k > -1:
                if counter >= 2:
                    break
                if text[second_part_boyer_moore[i] - len(first_part) + k] != pat[j]:  # substitution
                    counter += 1
                    # Diagonal checking
                    if text[second_part_boyer_moore[i] - len(first_part) + k - 1] == pat[j]:
                        j += 1
                    if text[second_part_boyer_moore[i] - len(first_part) + k] == pat[j - 1]:
                        k += 1
                k -= 1
                j -= 1
            if counter <= 1:
                edit_dist_list.append([second_part_boyer_moore[i] - len(first_part), counter])
            i += 1

    if len(edit_dist_list) > 0:    # If there exists patterns <= 1 edits only then we will create unique list
        filtering_duplicates = []
        # This list stores all the unique values and does not take the duplicates
        for items in edit_dist_list:
            if items not in filtering_duplicates:
                filtering_duplicates.append(items)

        # Calling MergeSort to filter the duplicates
        # print(len(filtering_duplicates))
        merge_sort(filtering_duplicates)

        f = open('output_editdist.txt', 'w')
        for a, b in filtering_duplicates:
            f.write('{:>0} {:>1}\n'.format(a, b))
        f.close()



import argparse
def read_from_cmd():
    """
    This function takes input from the command line and then inserts the contents of the file to strings.
    :return:
    """
    a_variable = argparse.ArgumentParser()
    a_variable.add_argument('text_file', type=argparse.FileType('r'))
    a_variable.add_argument('pat_file', type=argparse.FileType('r'))
    args = a_variable.parse_args()
    text = ""
    pat = ""
    for item in args.text_file.read():
        text += item.strip()
    for items in args.pat_file.read():
        pat += items.strip()
    return text, pat

if __name__ == "__main__":
    text, pat = read_from_cmd()
    if len(pat) == 1:
        print("Since the length of pattern is 1, it prints all the occurrences of pattern in text")
        print(BoyerMoore(text, pat))
    elif len(pat) > len(text):
        print("Enter a pattern whose length is smaller than text")
        exit()
    else:
        edit_dist()

