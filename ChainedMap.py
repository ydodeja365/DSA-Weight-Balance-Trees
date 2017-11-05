# Todo make constructors & method similar to main HashMap 
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
        while tmp is not None and tmp.value[0] != x:
            tmp = tmp.next
        return tmp

    def keys(self):
        key_list = []
        tmp = self.head
        while tmp is not None:
            key_list.append(tmp.value[0])
            tmp = tmp.next
        return key_list


class HashMap:
    def __init__(self):
        self.arr = [None for _ in range(30)]

    @staticmethod
    def hash(key):
        h = 0
        x = 33
        for ch in key:
            h *= x
            h += ord(ch)
        return h % 30

    def insert(self, tup):
        hkey = self.hash(tup[0])
        if self.arr[hkey] is None:
            self.arr[hkey] = LinkedList()
        self.arr[hkey].insert_head(tup)

    def search(self, key):
        hkey = self.hash(key)
        return self.arr[hkey].search(key)

    def keys(self):
        ks = []
        for linked_list in self.arr:
            if linked_list is not None:
                ks += linked_list.keys()
        return ks
