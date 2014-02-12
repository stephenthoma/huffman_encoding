from math import floor

class PriorityQueue:
    """Implementation of a Priority Queue using a Max Heap for storage."""

    def __init__(self):
        self.queue = list()

    def parent(self, index):
        return int(floor(index / 2))

    def heapify(self, index):
        """Maintains the heap invariant. O(log(n))"""
        left_index  = 2 * index + 1
        right_index = 2 * index + 2

        largest = index
        if left_index < len(self.queue) and self.queue[left_index][0] > self.queue[index][0]:
            largest = left_index
        if right_index < len(self.queue) and self.queue[right_index][0] > self.queue[largest][0]:
            largest = right_index

        if largest != index:
            self.queue[index], self.queue[largest] = self.queue[largest], self.queue[index]
            self.heapify(largest)

    def proc_up(self, index):
        """If node is larger than parent, swap. O(log(n))"""
        while index != 0 and self.queue[self.parent(index)][0] < self.queue[index][0]:
            self.queue[index], self.queue[self.parent(index)] = self.queue[self.parent(index)], self.queue[index]
            index = self.parent(index)

    def insert(self, ele):
        """Insert element into heap, insuring invariant is maintained. O(log(n))"""
        self.queue.append(ele)
        self.proc_up(len(self.queue) - 1)

    def extract_max(self):
        """Remove top element, then reheapify. O(log(n))"""
        maximum = self.queue[0]
        data = self.queue.pop()
        if len(self.queue) > 0: # Reheapify if there's still elements left.
            self.queue[0] = data
            self.heapify(0)
        return maximum