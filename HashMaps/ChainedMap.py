class ListNode:
    def __init__(self, value=None, nxt=None):
        self.value = value
        self.next = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, x):
        self.head = ListNode(x, self.head)

    def search(self, x):
        tmp = self.head
        while tmp is not None and tmp.value.key != x:
            tmp = tmp.next
        return tmp.value


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
        hkey = self.hash(pair.key)
        if self.arr[hkey] is None:
            self.arr[hkey] = LinkedList()
        self.arr[hkey].insert_head(pair)

    def search(self, key):
        hkey = self.hash(key)
        return self.arr[hkey].search(key)
