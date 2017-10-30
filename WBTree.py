class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.weight = 1

    def refresh_weight(self):
        if self is None:
            return
        left_weight = 0 if self.left is None else self.left.weight
        right_weight = 0 if self.right is None else self.right.weight
        self.weight = left_weight + right_weight + 1


class WBT:
    def __init__(self):
        self.root = None
        self.alpha = 1

    def insert(self, val):
        pass

    def search(self, val):
        pass

    def delete(self, node):
        pass

    def print(self):
        pass