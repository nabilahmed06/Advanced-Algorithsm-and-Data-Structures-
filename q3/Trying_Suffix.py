
class Node:
    def __init__(self):
        """
        counter = pointer back to the original list
        time = number of times a node is visited for calculating number of words with same prefix
        """
        self.array = [None] * 26
        self.frequency = 0
        self.counter = 0
        self.time = 0
        self.ending = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert_word(self, word, f, c):
        """
        :param word: word to be passed from the dictionary
        :param f: frequency
        :param c: pointer back to my original list
        :return: None
        """
        temp = self.root
        for item in word:
            # if object at node exists
            # if the frequency of the word being inserted is greater than the current frequency of node
            # then update frequency and pointer
            # increment counter irrespectively
            if temp.array[ord(item) - ord("a")] is not None:
                if temp.frequency < f:
                    temp.frequency = f
                    temp.counter = c
                temp.time += 1
                temp = temp.array[ord(item) - ord("a")]
            else:
                # if object at node does not exist
                # make a new node
                # put in the frequency, pointer, counter
                temp.array[ord(item) - ord("a")] = Node()
                temp.frequency = f
                temp.counter = c
                temp.time += 1
                temp = temp.array[ord(item) - ord("a")]

        temp.ending = True

    def prefix(self, word):
        traverse = self.root
        for item in word:
            # while node is not none and keeps pointing to new node
            # keep on traversing
            if traverse.array[ord(item) - ord("a")] is not None:
                traverse = traverse.array[ord(item) - ord("a")]
            else:
                # if word not found return False
                return False

        return traverse.frequency, traverse.counter, traverse.time

