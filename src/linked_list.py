class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def to_list(self):
        """
        Возвращает список с данными, содержащимися в односвязном списке `LinkedList
        """
        data_list = []
        node = self.head
        while node:
            data_list.append(node.data)
            node = node.next_node
        return data_list

    def get_data_by_id(self, data_id):
        """
        Возвращает первый найденный в `LinkedList` словарь с ключом 'id',
        значение которого равно переданному в метод значению.
        """
        node = self.head
        while node:
            try:
                if isinstance(node.data, dict) and "id" in node.data and node.data["id"] == data_id:
                    return node.data
                else:
                    node = node.next_node
                raise TypeError
            except TypeError:
                print("Данные не являются словарем или в словаре нет ключа 'id'")

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return "None"

        ll_string = ""
        while node:
            ll_string += f"{str(node.data)} -> "
            node = node.next_node
        ll_string += "None"
        return ll_string
