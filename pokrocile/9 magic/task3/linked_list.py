class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList():
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0
