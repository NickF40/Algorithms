import time


class CountingSort:
    def __init__(self, *values):
        self.values = values
        self.temp = [0]
        self.result = [0] * len(values)

    def sort(self, k):
        st_time = time.time()
        self.temp *= k
        for i in self.values:
            self.temp[i] += 1
        for i in range(1, k):
            self.temp[i] += self.temp[i-1]

        for j in range(len(self.values)-1, -1, -1):
            self.result[self.temp[self.values[j]]-1] = self.values[j]
            self.temp[self.values[j]] -= 1
        fin_time = time.time()
        print("Sorting took %f seconds" % (fin_time - st_time))
        return self.result


cs = CountingSort(6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2)
print(cs.sort(7))



