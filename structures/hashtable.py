import numpy as np
import ctypes
import gc


class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


class Node:
    def __init__(self, value, parent, descendant):
        self.value = value
        self.parent = parent
        self.descendant = descendant

    def __next__(self):
        return self.parent

    def __str__(self):
        return str(self.value)


class ListIterator:
    def __init__(self, first):
        self.first = first

    def __next__(self):
        if self.first:
            return_value = self.first.value
            self.first = self.first.descendant
            return return_value
        else:
            raise StopIteration()


class LinkedList:
    def __init__(self, *values):
        last = None
        cur = None
        for value in values:
            cur = Node(value, last, None)
            if last:
                if last == self.first:
                    self.first.descendant = cur
                last.descendant = cur
            else:
                self.first = cur
            last = cur
        self.last = cur

    def append(self, value):
        cur = Node(value, self.last, None)
        if not self.last:
            self.first = cur
            self.last = cur
        else:
            self.last.descendant = cur
            self.last = cur

    def prepend(self, value):
        node = Node(value, None, self.first)
        self.first.parent = node
        self.first = node

    def pop(self):
        if self.last:
            return_value = self.last.value
            self.last.parent.descendant = None
            parent = self.last.parent
            del self.last
            self.last = parent
            return return_value
        else:
            return None

    def find(self, n, node=None):
        if n < 0:
            return node
        if not node:
            return self.find(n-1, node=self.first)
        elif node.descendant:
            return self.find(n-1, node=node.descendant)
        else:
            return node

    def remove(self, n):
        node = self.find(n)
        if node:
            node.parent.descendant = node.descendant
            node.descendant.parent = node.parent
            del node
        else:
            return None

    def __str__(self):
        str_ = "["
        cur = self.first
        while True:
            str_ += str(cur) + ", "
            if cur.descendant:
                cur = cur.descendant
            else:
                return str_[:-2] + "]"

    def __iter__(self):
        return ListIterator(self.first)


class HashTable:
    def __init__(self, *pairs):
        # Python automatically removes all objects with no links to them
        # So we have to use this to prevent this from happening
        self.links_saver = []
        try:
            self.array = np.zeros((10000000,), dtype=int)
        except Exception as e:
            print(e)
            exit(-1)
        gc.disable()
        if pairs:
            for pair in pairs:
                self.add(pair[0], pair[1])

    @staticmethod
    def very_simple_hash(value):
        if isinstance(value, str):
            res = 1
            for ch_ in value:
                res *= ord(ch_)
            return res * len(value)
        elif isinstance(value, int):
            return value * len(str(value))

    def add(self, key, value):
        if not self.array[self.very_simple_hash(key)]:
            my_list = LinkedList()
            my_list.prepend((key, value))
            self.links_saver.append(my_list)
            self.array[self.very_simple_hash(key)] = int(id(my_list))
            # uncomment to see num of references
            # print(PyObject.from_address(int(self.array[self.very_simple_hash(key)])).refcnt)
        else:
            llist = ctypes.cast(int(self.array[self.very_simple_hash(key)]), ctypes.py_object).value
            llist.prepend((key, value))

    def get(self, key):
        # uncomment to see num of references
        # print(PyObject.from_address(int(self.array[self.very_simple_hash(key)])).refcnt)
        llist = ctypes.cast(int(self.array[self.very_simple_hash(key)]), ctypes.py_object).value
        for key_, val_ in llist:
            if key_ == key:
                return val_
        return None




        

