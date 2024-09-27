import pytest

from priority_queue import PriorityQueue


def test_push():
    pq = PriorityQueue()
    pq.push("Task 1", 3)
    pq.push("Task 2", 1)
    pq.push("Task 3", 2)
    assert len(pq) == 3


def test_pop():
    pq = PriorityQueue()
    pq.push("Task 1", 3)
    pq.push("Task 2", 1)
    pq.push("Task 3", 2)
    pq.push("Task 4", 5)
    pq.push("Task 5", 6)

    assert pq.pop() == "Task 2"
    assert len(pq) == 4


def test_empty_pop():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_iteration():
    pq = PriorityQueue()
    pq.push("Task 1", 3)
    pq.push("Task 2", 1)
    pq.push("Task 3", 2)
    pq.push("Task 4", 5)
    pq.push("Task 5", 6)

    tasks = list(pq)
    assert tasks == ["Task 2", "Task 3", "Task 1", "Task 4", "Task 5"]
