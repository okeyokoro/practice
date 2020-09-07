from math import sqrt


def calculate_distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2
                + (p2[1] - p1[1])**2)


class MaxHeap():
    def __init__(self, mx=float("inf")):
        self.heap = []
        self.max = mx

    @property
    def head(self):
        if self.heap:
            return self.heap[0]
        return None

    @property
    def size(self):
        return len(self.heap)

    # log(n)
    def decide(self, num):
        if self.size < self.max:
            self.insert(num)
            return

        if num[0] >= self.head[0]:
            return

        self.pophead()
        self.insert(num)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def get_parent_idx(self, idx):
        return (idx-1)//2

    def get_first_child_idx(self, idx):
        return idx*2+1

    def get_second_child_idx(self, idx):
        return idx*2+2 if idx*2+2 <= self.size-1 else -1

    # log(n)
    def pophead(self):
        # swap the head with the tail
        self.swap(0, self.size-1)
        # drop the tail
        self.heap.pop()
        self.bubble_down()

    # log(n)
    def insert(self, element):
        self.heap.append(element)
        self.bubble_up()

    # log(n)
    def bubble_up(self):
        """ take the tail element to it's rightful place """
        idx = self.size-1
        pidx = self.get_parent_idx(idx)

        while pidx > 0:
            child_is_greater_than_parent = self.heap[idx] > self.heap[pidx]
            if child_is_greater_than_parent:
                self.swap(idx, pidx)
                idx = pidx
                pidx = self.get_parent_idx(idx)
                continue

            return

    # log(n)
    def bubble_down(self):
        """ take the head element to it's rightful place """
        idx = 0
        c1_idx = self.get_first_child_idx(idx)

        while c1_idx <= self.size-1:
            c2_idx = self.get_second_child_idx(idx)

            # select which child to swap
            if c2_idx > 0 and self.heap[c2_idx] < self.heap[c1_idx]:
                idx_to_swap = c2_idx
            else:
                idx_to_swap = c1_idx

            child_is_greater_than_parent = self.heap[idx_to_swap] > self.heap[idx]
            if child_is_greater_than_parent:
                self.swap(idx, idx_to_swap)
                idx = idx_to_swap
                c1_idx = self.get_first_child_idx(idx)
                continue

            return


def quickselect(k, arr, pivot=1):
    low = []
    mid = []
    hig = []

    for num in arr:
        if num > arr[pivot]:
            high.append(num)
        elif num < arr[pivot]:
            low.append(num)
        else:
            mid.append(num)

    if len(low) == k:
        return low
    elif len(low) < k:
        k_closet_sort(k, low+mid)
    else:
        k_closet_sort(k, low)


class Solution:
    def kClosest(self, points, k_closest, vertex=[0,0]):
        h = MaxHeap(k_closest)

        for point in points:
            t = [calculate_distance(point, vertex), point]
            h.decide(t)

        return [ i[1] for i in h.heap ]

        # we don't need to sort the full array
        # since we only need the k smallest

        # time-complexity:
        #   - worst-case: O(N*logN)
        #   - best-case: O(N*k)

        # space complexity: O(k)