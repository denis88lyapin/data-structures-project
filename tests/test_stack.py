import unittest

from src.stack import Node, Stack


class NodeTest(unittest.TestCase):
    def test_node_creation(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)

        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)

        self.assertEqual(n2.data, 'a')
        self.assertEqual(n2.next_node, n1)

    def test_node_data(self):
        n = Node(5, None)
        self.assertEqual(n.data, 5)


class StackTest(unittest.TestCase):
    def test_stack_creation(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

    def test_stack_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')

        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')
        self.assertEqual(stack.top.next_node.next_node, None)

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        self.assertEqual(stack.pop(), 'data3')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.pop(), 'data2')
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(stack.pop(), 'data1')
        self.assertEqual(stack.top, None)

    def test_stack_pop_empty_stack(self):
        stack = Stack()
        with self.assertRaises(AttributeError):
            stack.pop()

    def test_stack_str(self):
        stack = Stack()
        self.assertEqual(str(stack), 'Стек пустой')
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(str(stack), 'Стек: data2, data1')
