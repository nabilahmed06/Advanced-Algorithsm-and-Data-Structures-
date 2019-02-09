class Node():
    def __init__(self, index, start, end, link):
        self.index = index
        self.start = start
        self.end = end
        self.link = link

class suffix_tree():
    def __init__(self, string):
        """
        take a string and construct a suffix array
        :param string:
        """
        self.root = Node(-1, -1, -1, -1)
        self.string = string
        self.array = []
        for i in range(256):
            self.array.append(0)
        current = self.root
        for i in range(len(self.string)):
            self.ukkonen(i)

    def ukkonen(self, i):




if __name__ == "__main__":
    a = suffix_tree("abcd")
    print(a.array)
    print(a.string)
    print(a.root)
