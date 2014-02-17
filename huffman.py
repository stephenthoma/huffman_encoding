from sys import argv

class PriorityQueue:
    """Implementation of a Priority Queue using a Max Heap for storage."""

    def __init__(self):
        self.queue = list()

    def parent(self, index):
        return index / 2

    def heapify(self, index):
        """Maintains the heap invariant. O(log(n))"""
        left_index  = 2 * index + 1
        right_index = 2 * index + 2

        largest = index
        if left_index < len(self.queue) and self.queue[left_index][0] < self.queue[index][0]:
            largest = left_index
        if right_index < len(self.queue) and self.queue[right_index][0] < self.queue[largest][0]:
            largest = right_index

        if largest != index:
            self.queue[index], self.queue[largest] = self.queue[largest], self.queue[index]
            self.heapify(largest)

    def proc_up(self, index):
        """If node is larger than parent, swap. O(log(n))"""
        while index != 0 and self.queue[self.parent(index)][0] > self.queue[index][0]:
            self.queue[index], self.queue[self.parent(index)] = self.queue[self.parent(index)], self.queue[index]
            index = self.parent(index)

    def insert(self, ele):
        """Insert element into heap, insuring invariant is maintained. O(log(n))"""
        self.queue.append(ele)
        self.proc_up(len(self.queue) - 1)

    def extract_min(self):
        """Remove top element, then reheapify. O(log(n))"""
        maximum = self.queue[0]
        data = self.queue.pop()
        if len(self.queue) > 0: # Reheapify if there's still elements left.
            self.queue[0] = data
            self.heapify(0)
        return maximum

class huffmanNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

class HuffmanEncode:
    """Implementation of Huffman Encoding."""
    def __init__(self):
        self.codebook = {}

    def get_frequencies(self, string):
        """
        Finds the frequency with which characters appear in a string, and
        returns them in a list of tuples of the form (frequency, character).
        """
        freqs = {}
        for char in string:
            freqs[char] = freqs.get(char, 0) + 1

        out = sorted([(f, c) for c, f in freqs.items()])
        return out

    def make_tree(self, freqs):
        """Create a Huffman tree for a given set of characters and frequencies."""
        pq = PriorityQueue()

        for val in freqs:
            pq.insert(val)
        while len(pq.queue) > 1:
            l, r = pq.extract_min(), pq.extract_min()
            node = huffmanNode(l, r)
            pq.insert((l[0]+r[0], node))

        return pq.queue[0]

    def make_codes(self, node, code=''):
        """Generate a set of Huffman codes from a Huffman tree."""
        node = node[1] # Discard frequency information

        if isinstance(node, basestring):
            self.codebook[node] = code
            return

        code+='0'
        self.make_codes(node.left, code)
        code = code[:-1]+'1'
        self.make_codes(node.right, code)

    def encode_string(self, string):
        """Huffman encode a string."""
        if not len(self.codebook) > 0:
            print("Must run make_codes() first!")
            return

        encoding = ""
        for x in string:
            code = self.codebook[x]
            encoding += code

        return encoding

if __name__ == "__main__":
    if len(argv) < 1:
        print("Usage: python huffman.py <string to encode>")

    string = argv[1]
    huff = HuffmanEncode()

    huff.make_codes(huff.make_tree(huff.get_frequencies(string)))
    print(huff.codebook)
    print(huff.encode_string(string))