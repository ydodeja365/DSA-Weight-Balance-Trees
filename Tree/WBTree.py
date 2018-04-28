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

    def leaf(self):
        return self.left is None and self.right is None

    @staticmethod
    def weight(node):
        return 0 + 1 if node is None else node.size + 1

    @staticmethod
    def size(node):
        return 0 if node is None else node.size

    def balanced(self):
        return 1 / 3 <= Node.weight(self.left) / Node.weight(self.right) <= 3

    def __str__(self):
        return str((self.val, self.size))


class WBT:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return self.root
        node_parent = self.root
        tmp = self.root
        while tmp is not None and tmp.val != val:
            node_parent = tmp
            tmp = tmp.left if val < tmp.val else tmp.right
        if tmp is not None:
            tmp.val = val
            return tmp
        node = Node(val, node_parent)
        if node.val < node_parent.val:
            node_parent.left = node
        else:
            node_parent.right = node
        while node_parent is not None:
            if not node_parent.balanced():
                node_parent = self.balance(node_parent)
            else:
                node_parent.refresh_weight()
            node_parent = node_parent.parent
        return node

    def delete(self, val):
        node = self.search(val)
        if node is not None:
            self.delete_node(node)
        return node

    def delete_node(self, node):
        if node.left is None or node.right is None:
            replacement = node.left if node.right is None else node.right
            node_parent = node.parent
            if replacement is not None:
                replacement.parent = node_parent
            if node_parent is None:
                self.root = replacement
                return
            if node.val < node_parent.val:
                node_parent.left = replacement
            else:
                node_parent.right = replacement
            while node_parent is not None:
                if not node_parent.balanced():
                    node_parent = self.balance(node_parent)
                else:
                    node_parent.refresh_weight()
                node_parent = node_parent.parent
        else:
            successor = self.min(node.right)
            node.val = successor.val
            self.delete_node(successor)

    @staticmethod
    def min(node):
        while node.left is not None:
            node = node.left
        return node

    def balance(self, node):
        if Node.weight(node.left) * 3 < Node.weight(node.right):
            if Node.weight(node.left) < 2 * Node.weight(node.right):
                return self.rotate_left(node)
            if Node.weight(node.left) >= 2 * Node.weight(node.right):
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        if Node.weight(node.right) * 3 < Node.weight(node.left):
            if Node.weight(node.right) < 2 * Node.weight(node.left):
                return self.rotate_right(node)
            if Node.weight(node.right) >= 2 * Node.weight(node.left):
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        return node

    def rotate_right(self, z):
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

    def present(self, val):
        return self.search(val) is not None

    def search(self, val):
        tmp = self.root
        while tmp is not None and tmp.val != val:
            tmp = tmp.left if val < tmp.val else tmp.right
        return tmp

    def print(self, root, space):
        if root is None:
            return
        space += 5
        self.print(root.right, space)
        print(' ' * space, end='')
        print(root)
        self.print(root.left, space)

    @staticmethod
    def swap(x, y):
        # Todo swap nodes instead of copy
        pass

    def __str__(self):
        self.print(self.root, -5)
        return ''

    def kth(self, k, root=None):
        if root is None:
            root = self.root
        if Node.size(root.left) + 1 == k:
            return root
        if Node.size(root.left) >= k:
            return self.kth(k, root.left)
        return self.kth(k - Node.size(root.left) - 1, root.right)

    def pre_order(self, root=None):
        if root is None:
            root = self.root
        if root is None:
            return
        yield root.val
        if root.left is not None:
            yield from self.pre_order(root.left)
        if root.right is not None:
            yield from self.pre_order(root.right)

    def post_order(self, root=None):
        if root is None:
            root = self.root
        if root is None:
            return
        if root.left is not None:
            yield from self.post_order(root.left)
        if root.right is not None:
            yield from self.post_order(root.right)
        yield root.val

    def in_order(self, root=None):
        if root is None:
            root = self.root
        if root is None:
            return
        if root.left is not None:
            yield from self.in_order(root.left)
        yield root.val
        if root.right is not None:
            yield from self.in_order(root.right)

    def reverse_in_order(self, root=None):
        if root is None:
            root = self.root
        if root is None:
            return
        if root.right is not None:
            yield from self.reverse_in_order(root.right)
        yield root.val
        if root.left is not None:
            yield from self.reverse_in_order(root.left)

    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return -1
        return self.height_internal(node) - 1

    def height_internal(self, node):
        if node is None:
            return 0
        if node.leaf():
            return 1
        return 1 + max(self.height_internal(node.left), self.height_internal(node.right))
