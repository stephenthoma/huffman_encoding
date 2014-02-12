import unittest
from huf import PriorityQueue

class priorityQueueTests(unittest.TestCase):
    def test_insert(self):
        pq = PriorityQueue()
        pq.insert((5, 'b'))
        pq.insert((8, 'c'))
        pq.insert((1, 'a'))

        result = [(8, 'c'), (5, 'b'), (1, 'a')]
        self.assertEqual(pq.queue, result)

    def test_extract_max(self):
        pq = PriorityQueue()
        pq.insert((8, 'b'))
        pq.insert((3, 'a'))

        result = (8, 'b')
        self.assertEqual(pq.extract_max(), result)

if __name__ == "__main__":
    unittest.main()