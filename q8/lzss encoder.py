"""
Nabil Ahmed
ID: 25364170
Task 4
This is an incomplete implementation of the LZ77
This does not work
P.S: Was trying it out in the last moment
"""

f = open('textfile.txt', 'r')
print(f)

a = ""

for items in f:
    a += items

dictionary = 6
buffer = 4


def encoding_string(a_string, w, b):
    encoder = []   # will store the triple
    # i is my pos
    i = 0
    w = i - w
    b += i

    while i < len(a_string):
        if w <= 0:  # dict pointer is negative
            len_max_substring = 0
            store_offset = None
            len_substring = 0
            while i <= b:
                j = 0
                while j <= b:
                    if a_string[i] == a_string[j]:
                        len_substring += 1
                        i += 1
                        j += 1

                    if len_substring > len_max_substring:
                        len_max_substring = len_substring
                        store_offset = j


                    j += 1

                # offset, length, next character to be read
                encoder.append([])

        i += 1
        return encoder

