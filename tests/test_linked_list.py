import unittest
from src.linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def test_linked_list(self):
        # Создаем пустой список
        ll = LinkedList()

        # Проверяем пустой список
        self.assertEqual(str(ll), "None")

        # Добавляем узлы в начало списка
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})

        # Проверяем список после добавления узлов в начало
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> None")

        # Добавляем узлы в конец списка
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})

        # Проверяем список после добавления узлов в конец
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
