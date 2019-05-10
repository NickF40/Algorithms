"""
Inspired by:


Introduction to Algorithms(1990)

By:
Thomas H. Cormen
Charles E. Leiserson
Ronald L. Rivest
Clifford Stein
"""

import time


class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def __repr__(self):
        return str(self.key)


class BinaryTree:
    def __init__(self, *values):
        self.root = Node(values[0], None)
        for value in values[1:]:
            self.insert_node(Node(value, None))

    @staticmethod
    def iterative_search(x, k):
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def search(self, x, k):
        if x is None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    @staticmethod
    def minimum(x):
        while x.left is not None:
             x = x.left
        return x

    @staticmethod
    def maximum(x):
        while x.right is not None:
            x = x.right
        return x

    def successor(self, x):
        if x.right is not None:
            return self.minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def successor(self, x):
        if x.right:
            return self.minimum(x)
        else:
            y = x.parent
            while y and y.right == x:
                x = y
                y = y.parent
        return y

    def insert_node(self, z):
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if not y:
            self.root = z   # Empty tree
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

    def _inorder_tree_walk(self, x):
        if x:
            self._inorder_tree_walk(x.left)
            print(x)
            self._inorder_tree_walk(x.right)

    def print(self):
        self._inorder_tree_walk(self.root)


tree = BinaryTree(15, 5, 18, 17, 20, 7, 3, 4, 2, 13, 9)
tree.print()