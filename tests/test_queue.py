import unittest
from src.queue import Queue


class QueueTests(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

        queue.enqueue('data1')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.tail.data, 'data1')
        self.assertIsNone(queue.head.next_node)
        self.assertIsNone(queue.tail.next_node)

        queue.enqueue('data2')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.tail.data, 'data2')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertIsNone(queue.tail.next_node)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        data = queue.dequeue()
        self.assertEqual(data, 'data1')
        self.assertEqual(queue.head.data, 'data2')

        data = queue.dequeue()
        self.assertEqual(data, 'data2')
        self.assertEqual(queue.head.data, 'data3')

        data = queue.dequeue()
        self.assertEqual(data, 'data3')
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

        self.assertRaises(AttributeError, queue.dequeue)

    def test_str(self):
        queue = Queue()
        self.assertEqual(str(queue), "")

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(str(queue), "data1\ndata2\ndata3")
