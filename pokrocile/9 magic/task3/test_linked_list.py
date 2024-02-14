import pytest

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
    assert linked_list.tail.data == 3


def test_iteration():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    items = list(linked_list)
    assert items == [1, 2, 3]


@pytest.fixture
def sample_doubly_linked_list():
    dll = DoublyLinkedList()
    dll.insert(1, 0)
    dll.insert(2, 1)
    dll.insert(3, 2)
    return dll


def test_insert_at_beginning(sample_doubly_linked_list):
    sample_doubly_linked_list.insert(0, 0)
    assert sample_doubly_linked_list.head.data == 0
    assert sample_doubly_linked_list.head.next_node.data == 1


def test_insert_at_middle(sample_doubly_linked_list):
    sample_doubly_linked_list.insert(4, 2)
    assert sample_doubly_linked_list.head.next_node.next_node.data == 4
    assert sample_doubly_linked_list.head.next_node.next_node.next_node.data == 3


def test_insert_at_end(sample_doubly_linked_list):
    sample_doubly_linked_list.insert(5, 3)
    current = sample_doubly_linked_list.head
    while current.next_node:
        current = current.next_node
    assert current.data == 5
    assert current.prev_node.data == 3


def test_insert_invalid_position(sample_doubly_linked_list):
    with pytest.raises(IndexError):
        sample_doubly_linked_list.insert(99, 5)
