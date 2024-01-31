from linked_list import DoublyLinkedList


def test_length():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert len(linked_list) == 3

def test_get_item():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list[0] == 1

def test_set_item():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list[0] = 0
    assert linked_list[0] == 0

def test_del_item():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    del linked_list[1]
    assert len(linked_list) == 2
    assert linked_list[1] == 3

def test_iteration():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    items = list(linked_list)
    assert items == [1, 2, 3]
