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

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        result = ll.get_data_by_id(2)
        expected = {'id': 2, 'username': 'mosh_s'}
        self.assertEqual(result, expected)

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})

        result = ll.to_list()
        expected = [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'},
                    {'id': 3, 'username': 'mosh_s'}]
        self.assertEqual(result, expected)

    def test_get_data_by_id_invalid_data(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'userna'
                                   'me': 'mosh_s'})

        result = ll.get_data_by_id(4)
        expected = None
        self.assertEqual(result, expected)
