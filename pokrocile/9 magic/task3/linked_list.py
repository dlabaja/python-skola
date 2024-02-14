class Node:
    def __init__(self, prev_node=None, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkedList:
    def __init__(self):
        super().__init__()
        self.head: Node = None
        self.tail: Node = None
        self.length = 0

    def append(self, data):
        if len(self) == 0:
            node = Node(None, data, None)
            self.head = node
            self.tail = node
            self.length += 1
            return

        node = Node(self.tail, data, None)
        self.tail.next_node = node
        self.tail = node
        self.length += 1

    def insert(self, data, index):
        # todo záporné indexy
        if index > self.length:
            raise IndexError

        if index == self.length:  # na konci
            self.append(data)
            return

        if index == 0:  # na začátku
            if len(self) == 0:
                self.append(data)
                return

            node = Node(None, data, self.head)
            self.head.prev_node = node
            self.head = node
            self.length += 1
            return

        prev_node = self.get_node(index - 1)
        node = Node(prev_node, data, prev_node.next_node)
        prev_node.next_node.prev_node = node
        prev_node.next_node = node
        self.length += 1

    def __iter__(self):
        ls = [self.head.data]
        last = self.head
        for _ in range(len(self) - 1):
            ls.append(last.next_node.data)
            last = last.next_node

        return iter(ls)

    def get_node(self, index) -> Node:
        last = self.head
        if index == 0:
            return last

        for i in range(len(self) - 1):
            if i == index - 1:
                return last.next_node
            last = last.next_node

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return list(self)[index]

    def __setitem__(self, index, data):
        self.get_node(index).data = data

    def __delitem__(self, index):
        node = self.get_node(index)
        prev = node.prev_node
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = prev
        self.length -= 1
