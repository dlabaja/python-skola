class Node:
    def __init__(self, next_node=None, data=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        self.length += 1

        if self.length == 0:
            self.head = Node(data)
            self.tail = Node(data)
            return

        self.tail = Node(self.tail, data, None)

    def insert(self, data, index):
        # todo přidat záporné indexy
        if self.length < index < 0:
            raise IndexError

        if index == self.length:  # vlož na konec
            self.append(data)
            return

        if index == 0:  # vlož na začátek
            node = Node(None, data, self.head)
            self.head.prev_node = node
            self.head = node
            return

        # vlož na konec
        node = Node(self[index - 1], data, self[index + 1])
        self[index - 1].next_node = node
        self[index + 1].prev_node = node


    def __delitem__(self, index):
        pass

    def __len__(self):
        return self.length

    def __iter__(self):
        lst = [self.head]
        last = self.head
        for _ in range(self.length):
            lst.append(last.next_node)

        return lst

    def __getitem__(self, key):
        return list(self.__iter__())[key]

    def __setitem__(self, key):
        pass
