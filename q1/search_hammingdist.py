"""
Q1
Nabil Ahmed
ID: 25364170
hamming distance
"""

from mergesort import merge_sort
from Boyer_Moore import BoyerMoore


def odd_or_even_length(pat_1):
    """
    Splits the pattern into 2 parts depending on the length of the pattern.
    :param pat_1:
    :return: Two parts of the pattern
    """
    if len(pat_1) % 2 == 0:  # even
        first_half = pat_1[:len(pat_1) // 2]
        second_half = pat_1[len(pat_1) // 2:len(pat_1)]
    else:   # odd
        first_half = pat_1[:len(pat_1) // 2]
        second_half = pat_1[len(pat_1) // 2:len(pat_1)]
    return first_half, second_half


def hamming_dist():
    """
    This function will find the hamming distance with <= 1
    It splits the words into 2 parts.
    Then it takes the First portion of the word.
    Does Boyer Moore on it to find all the exact occurrences.
    Then it accesses the portion of the TEXT that has the exact occurrences.
    And then iterates through the 2nd part of the pattern.
    It there are more than 1 mismatch it will not take that position.
    This theory is known as the pigeon hole principal.
    After doing the first part, it will also do the same thing with the 2nd part of the pattern.
    :return: List with hamming distance less than or equal to 1
    """
    split_word = odd_or_even_length(pat)   # splits word into 2 parts
    first_part = split_word[0]             # first part
    second_part = split_word[1]            # second part
    hamming_list = []                      #hamming list
    first_part_boyer_moore = BoyerMoore(text, first_part)

    if len(first_part_boyer_moore) > 0:   # if list is not empty only then it will check
        if first_part_boyer_moore[-1] + len(pat) > len(text):
            first_part_boyer_moore.remove(first_part_boyer_moore[-1])

        for items in first_part_boyer_moore:
            counter = 0
            for j in range(len(second_part)):
                if counter >= 2:
                    break

                if text[items + len(first_part) + j] != pat[len(first_part) + j]:
                    counter += 1
            if counter <= 1:
                hamming_list.append([items, counter])

    second_part_boyer_moore = BoyerMoore(text, second_part)  # 2nd part

    if len(second_part_boyer_moore) > 0:
        if second_part_boyer_moore[0] - len(first_part) < 0:
            second_part_boyer_moore.remove(second_part_boyer_moore[0])

        for items in second_part_boyer_moore:
            counter = 0
            for j in range(len(first_part)-1, -1, -1):
                if counter >= 2:
                    break
                if text[items - len(first_part) + j] != pat[j]:
                    counter += 1
            if counter <= 1:
                hamming_list.append([items - len(first_part), counter])

    if len(hamming_list) > 0:        # if list is not empty
        filtering_duplicates = []
        for items in hamming_list:
            if items not in filtering_duplicates:
                filtering_duplicates.append(items)

        filtering_duplicates = (merge_sort(filtering_duplicates))

        f = open('output_hammingdist.txt', 'w')
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
        hamming_dist()
