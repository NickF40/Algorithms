"""
Inspired by:


Introduction to Algorithms(1990)

By:
Thomas H. Cormen
Charles E. Leiserson
Ronald L. Rivest
Clifford Stein
"""


from time import time
from random import randint


class RandomizedQuicksort:
    def __init__(self, array):
        self.array = array

    def __call__(self, p, r):
        q = self.randomized_partition(p, r)
        if r > p:
            self(p, q-1)
            self(q+1, r)
        return self

    def __str__(self):
        return "%s\n" % str(self.array)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def randomized_partition(self, p, r):
        try:
            i = randint(p, r)
        except ValueError:
            return p
        self.swap(i, r)
        return self.partitionate(p, r)

    def partitionate(self, p, r):
        i = p - 1
        x = self.array[r]
        for j in range(p, r):
            if self.array[j] <= x:
                i += 1
                self.swap(i, j)
        if p < r:
            self.swap(i+1,   r)
        return i+1


qs = RandomizedQuicksort([14, 7, 12, 1, 0, 8, 6])
st_time = time()
print(qs(0, 6))
print("Sorting took %f seconds" % float(time() - st_time))
