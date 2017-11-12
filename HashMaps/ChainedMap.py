from HashMaps.Pair import *


class ListNode:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, x):
        self.head = ListNode(x, self.head)

    def search(self, x):
        tmp = self.head
        while tmp is not None and tmp.val != x:
            tmp = tmp.next
        return tmp.val

    def update(self, x):
        tmp = self.head
        while tmp is not None and tmp.val != x:
            tmp = tmp.next
        if tmp is None:
            self.insert_head(x)
            return False
        tmp.val = x
        return True


class ChainedHashMap:
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
        hkey = self.hash(pair.key)
        if self.arr[hkey] is None:
            self.arr[hkey] = LinkedList()
        self.arr[hkey].insert_head(pair)

    def search(self, key):
        hkey = self.hash(key)
        return self.arr[hkey].search(Pair(key))

    def update(self, pair):
        hkey = self.hash(pair.key)
        if self.arr[hkey] is None:
            self.arr[hkey] = LinkedList()
        return self.arr[hkey].update(pair)
