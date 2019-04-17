"""
Source:
Introduction to Algorithms(1990)

By:
Thomas H. Cormen
Charles E. Leiserson
Ronald L. Rivest
Clifford Stein
"""


from time import time


class Heapsort:
    def __init__(self, A):
        self.A = A
        self.heap_size = len(A) - 1

    @staticmethod
    def parent(i):
        return i/2

    @staticmethod
    def left(i):
        return i*2

    @staticmethod
    def right(i):
        return i*2+1

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l <= self.heap_size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i

        if r <= self.heap_size and self.A[r] > self.A[largest]:
            largest = r

        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(int(self.heap_size/2), -1, -1):
            self.max_heapify(i)

    def sort(self):
        st_time = time()
        self.build_max_heap()
        for i in range(self.heap_size, -1, -1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            self.heap_size -= 1
            self.max_heapify(0)
        end_time = time()
        print("Sorted:\t\t\t", self)
        print("Sorting of {n} elements took {delta} seconds".format(n=len(self.A), delta=float(end_time-st_time)))

    def __str__(self):
        return str(self.A)


if __name__ == "__main__":
    start_array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("Start array:\t", start_array)
    hs = Heapsort(start_array)
    hs.sort()
