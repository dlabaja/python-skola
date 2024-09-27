class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return f"Node({self.data})"


class DoublyLinkedList():
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        return "DoublyLinkedList({})".format(", ".join(str(item) for item in self))

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current_node = self._get_node_at_index(index)
        return current_node.data

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current_node = self._get_node_at_index(index)
        current_node.data = value

    def __delitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current_node = self._get_node_at_index(index)
        self._remove_node(current_node)

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, data, position):
        if position == len(self):
            self.append(data)
            return
        new_node = Node(data)

        if position == 0:
            new_node.next_node = self.head
            if self.head:
                self.head.prev_node = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Index out of range")
                current = current.next_node
            new_node.prev_node = current
            new_node.next_node = current.next_node
            if current.next_node:
                current.next_node.prev_node = new_node
            current.next_node = new_node
        self.length += 1

    def _get_node_at_index(self, index):
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next_node
        return current_node

    def _remove_node(self, node):
        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            self.head = node.next_node
        if node.next_node:
            node.next_node.prev_node = node.prev_node
        else:
            self.tail = node.prev_node
        self.length -= 1

# Příklad použití
linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Length:", len(linked_list))

print("Items:")
for item in linked_list:
    print(item)

print("First item:", linked_list[0])

# Odstraníme první prvek
del linked_list[0]

print("After deletion:")
for item in linked_list:
    print(item)
