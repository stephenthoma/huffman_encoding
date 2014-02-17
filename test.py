import unittest
from huffman import PriorityQueue
from huffman import HuffmanEncode

class priorityQueueTests(unittest.TestCase):
    def test_insert(self):
        pq = PriorityQueue()
        pq.insert((5, 'b'))
        pq.insert((8, 'c'))
        pq.insert((1, 'a'))

        result = [(1, 'a'), (5, 'b'), (8, 'c')]
        self.assertEqual(pq.queue, result)

    def test_extract_min(self):
        pq = PriorityQueue()
        pq.insert((8, 'b'))
        pq.insert((3, 'a'))

        result = (3, 'a')
        self.assertEqual(pq.extract_min(), result)

class huffmanEncodeTests(unittest.TestCase):
    def test_get_frequencies(self):
        huff = HuffmanEncode()
        result = [(1, 'a'), (2, 'b'), (3, 'A')]
        self.assertEqual(huff.get_frequencies("AAAbba"), result)

    def test_make_codes(self):
        huff = HuffmanEncode()
        node = huff.make_tree(huff.get_frequencies("AAAbba"))
        huff.make_codes(node)

        result = {'A': '0', 'a': '10', 'b': '11'}
        self.assertEqual(huff.codebook, result)

    def test_encode_string(self):
        huff = HuffmanEncode()
        node = huff.make_tree(huff.get_frequencies("AAAbba"))
        huff.make_codes(node)

        result = "000111110"
        self.assertEqual(huff.encode_string("AAAbba"), result)

if __name__ == "__main__":
    unittest.main()