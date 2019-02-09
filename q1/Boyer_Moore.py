"""
Nabil Ahmed
ID: 25364170
Boyer Moore
"""

from Zbox_Student import z_b_o_x


def BoyerMoore(text, pat):
    """
    Boyer Moore Algorithm takes a Text and Pattern both of type <String> and does exact pattern matching
    of the PAT on the TEXT. It uses the Bad Character Shift rule and the Good Suffix rule to efficiently
    shift while matching the pattern with text.
    :param text: Type<String>
    :param pat: Type<String>
    :return: List : Type<Numbers>
    """
    alphabets = []       # My Domain of ASCII characters will be stored in this list(Required for Bad Character)
    sub_list = [-1]
    for i in range(128):
        alphabets.append(sub_list)       # Initiating -1 as a sublist to my alphabets list

    print_array = []      # For storing the final result from the Boyer Moore Function

    for letter in range(len(pat)):
        alphabets_index = ord(pat[letter])
        if alphabets[alphabets_index][0] == -1:
            alphabets[alphabets_index].remove(-1)
        alphabets[alphabets_index].append(letter)

    zi_val = z_b_o_x(pat)   # Z values on my pat
    matched_prefix = []   # Matched Prefix Array

    for z in range(len(pat)):
        matched_prefix.append(0)

    if zi_val[len(zi_val)-1] == 0:
        for i in range(len(zi_val)-2, -1, -1):  # start from len - 2
            if zi_val[i] + i == len(pat):
                matched_prefix[i] = zi_val[i]
            else:
                matched_prefix[i] = matched_prefix[i + 1]
    else:  # right most value of zi is not equals to zero
        for i in range(len(zi_val)-1, -1, -1):  # start from len - 2
            if zi_val[i] + i == len(pat):
                matched_prefix[i] = zi_val[i]
            else:
                matched_prefix[i] = matched_prefix[i + 1]

    rev_pat = pat[::-1]
    zi_values = z_b_o_x(rev_pat)

    Zi_suffix = []
    for i in range(len(zi_values)-1, -1, -1):
        Zi_suffix.append(zi_values[i])

    goodsuffix = []
    for i in range(len(pat)):
        goodsuffix.append(0)

    i = 0
    while i < len(pat):
        if Zi_suffix[i] != 0:
            j = len(pat)- Zi_suffix[i] - 1
            goodsuffix[j] = i
        i += 1

    for i in range(len(pat), len(text) + 1):
        k = i - 1
        j = len(pat) - 1
        skp = 1    # normally skip by 1
        good_suffix_skip = 0
        bad_character_skp = 0
        while j >= 0:
            if text[k] != pat[j]:  # if mismatch occurs do Good suffix
                if j < len(pat) - 2:         # Good Suffix
                    if goodsuffix[j+1] > 0:
                        good_suffix_skip = len(pat) - goodsuffix[j+1]
                    if goodsuffix[j + 1] == 0:
                        good_suffix_skip = len(pat) - matched_prefix[j + 1]

                # Else:Bad Character:
                z = alphabets[ord(text[k])]
                for z1 in range(len(z) - 1, -1, -1):
                    if z[z1] < j:
                        bad_character_skp = j - z[z1]   # if bad character exists count the number of skips
                        break

                skp = max(good_suffix_skip, bad_character_skp)
                break

            j -= 1
            k -= 1

        if j == -1:  # If there is an exact match
            # return k+1    # k + 1 because we want the starting index of the matched pattern
            print_array.append(k + 1)
            # skp = len(pat) - matched_prefix[1]
        i += skp
    return print_array

# print(BoyerMoore(text_1, pat_1))
