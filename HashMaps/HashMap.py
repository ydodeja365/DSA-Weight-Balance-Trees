from HashMaps.Pair import Pair
from Tree.WBTree import WBT


class HashMap:
    def __init__(self, size):
        self.size = size
        self.arr = [None for _ in range(size)]

    def hash(self, key):
        h = 0
        x = 33
        for ch in key:
            h *= x
            h += ord(ch)
        return h % self.size

    def insert(self, pair):
        index = self.hash(pair.key)
        if self.arr[index] is None:
            self.arr[index] = WBT()
        self.arr[index].insert(pair)

    def search(self, key):
        index = self.hash(key)
        if self.arr[index] is None:
            return
        node = self.arr[index].search(Pair(key))
        if node is None:
            return
        return node.val
