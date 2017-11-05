class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
        self.size = 1

    def refresh_weight(self):
        if self is None:
            return
        left_size = 0 if self.left is None else self.left.size
        right_size = 0 if self.right is None else self.right.size
        self.size = left_size + right_size + 1
        return self.size + 1

    def is_leaf(self):
        return self.left is None and self.right is None

    @staticmethod
    def weight(node):
        return 0 + 1 if node is None else node.size + 1


class WBT:
    def __init__(self):
        self.root = None
        self.alpha = 1 - 1 / (2 ** .5)
        self.alpha = 0.29
        self.inner_alpha = self.alpha * (2 ** 0.5)

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
        z.refresh_weight()
        y.refresh_weight()
        if y.parent is not None:
            if y.val <= y.parent.val:
                y.parent.left = y
            else:
                y.parent.right = y
            y.parent.refresh_weight()
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
        z.refresh_weight()
        y.refresh_weight()
        if y.parent is not None:
            if y.val <= y.parent.val:
                y.parent.left = y
            else:
                y.parent.right = y
            y.parent.refresh_weight()
        else:
            self.root = y

        return y

    def insert_bin(self, val, root=None):
        if root is None:
            root = self.root
        if root is None:
            self.root = Node(val, root)
            return
        if val <= root.val:
            if root.left is None:
                root.left = Node(val, root)
            else:
                self.insert_bin(val, root.left)
        else:
            if root.right is None:
                root.right = Node(val, root)
            else:
                self.insert_bin(val, root.right)

    def insert_old(self, val, root=None):
        if root is None:
            root = self.root
        if self.root is None:
            self.root = Node(val, root)
            return self.root
        if val <= root.val:
            if root.left is None:
                root.left = Node(val, root)
                root.refresh_weight()
                return root
            root.left = self.insert_old(val, root.left)
            root.refresh_weight()
            if Node.weight(root.left) > (1 - self.alpha) * Node.weight(root):
                root = self.rotate_right(root)
        else:
            if root.right is None:
                root.right = Node(val, root)
                root.refresh_weight()
                return root
            root.right = self.insert_old(val, root.right)
            root.refresh_weight()
            if Node.weight(root.right) > (1 - self.alpha) * Node.weight(root):
                root = self.rotate_left(root)
        return root

    def insert(self, val, root=None):
        if self.root is None:
            self.root = Node(val, root)
            return self.root
        if root is None:
            root = self.root
        if val == root.val:
            root.val = val
            return root
        elif val < root.val:
            if root.left is None:
                root.left = Node(val, root)
                root.refresh_weight()
                return root
            root.left = self.insert(val, root.left)
        else:
            if root.right is None:
                root.right = Node(val, root)
                root.refresh_weight()
                return root
            root.right = self.insert(val, root.right)
        root.refresh_weight()
        root = self.balance(root)
        return root

    def balance(self, root):
        if Node.weight(root.left) > (1 - self.alpha) * Node.weight(root):
            if Node.weight(root.left.left) > self.inner_alpha * Node.weight(root.left):
                root = self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                root = self.rotate_right(root)
        elif Node.weight(root.left) < self.alpha * Node.weight(root):
            if Node.weight(root.right.left) < (1 - self.inner_alpha) * Node.weight(root.right):
                root = self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                root = self.rotate_left(root)
        return root

    def present(self, val):
        return self.search(val) is not None

    def search(self, val):
        tmp = self.root
        while tmp is not None and tmp.val != val:
            tmp = tmp.left if val < tmp.val else tmp.right
        return tmp

    def delete(self, node):
        pass

    def print_tree(self):
        self.print(self.root, -5)

    def print(self, root, space):
        if root is None:
            return
        space += 5
        self.print(root.right, space)
        print(' ' * space, end='')
        print((root.val, root.size))
        self.print(root.left, space)
