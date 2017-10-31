class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.size = 0

    def refresh_weight(self):
        if self is None:
            return
        left_size = 0 if self.left is None else self.left.size
        right_size = 0 if self.right is None else self.right.size
        self.size = left_size + right_size + 1
        return self.size + 1

    @staticmethod
    def weight(node):
        return 0 + 1 if node is None else node.size + 1


class WBT:
    def __init__(self):
        self.root = None
        self.alpha = 0.29

    def is_balanced(self, node):
        if node is None:
            return
        left_condition = Node.weight(node.left) >= self.alpha * Node.weight(node)
        right_condition = Node.weight(node.right) >= self.alpha * Node.weight(node)
        return left_condition and right_condition

    def rotate_right(self, z):
        if z is None:
            print('Got None in right rotate')
            return
        y = z.left
        z.left = y.right
        if y.right is not None:
            y.right.parent = z
        y.right = z
        y.parent = z.parent
        z.parent = y
        if y.parent is not None:
            if y.value <= y.parent.value:
                y.parent.left = y
            else:
                y.parent.right = y
        else:
            self.root = y
        return y

    def rotate_left(self, z):
        if z is None:
            print('Got None in left rotate')
            return
        y = z.right
        z.right = y.left
        if y.left is not None:
            y.left.parent = z
        y.left = z
        y.parent = z.parent
        z.parent = y
        if y.parent is not None:
            if y.value <= y.parent.value:
                y.parent.left = y
            else:
                y.parent.right = y
        else:
            self.root = y
        return y

    def insert(self, val):
        pass

    def present(self, val):
        return self.search(val) is not None

    def search(self, val):
        tmp = self.root
        while tmp is not None and tmp.val != val:
            tmp = tmp.left if val < tmp.val else tmp.right
        return tmp

    def delete(self, node):
        pass

    def print(self, root=None, space=None):
        if root is None:
            root = self.root
            space = 0
        if root is None:
            return
        space += 5
        WBT.print(root.right, space)
        i = 5
        while i < space:
            print(' ', end='')
            i += 1
        print(root.value)
        WBT.print(root.left, space)
