import pytest

from vector import Vector


@pytest.fixture
def vectors():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    return v1, v2


def test_addition(vectors):
    v1, v2 = vectors
    result = v1 + v2
    assert result == Vector(4, 6)


def test_subtraction(vectors):
    v1, v2 = vectors
    result = v1 - v2
    assert result == Vector(-2, -2)


def test_multiplication(vectors):
    v1, _ = vectors
    result = v1 * 3
    assert result == Vector(3, 6)


def test_equality(vectors):
    v1, v2 = vectors
    assert v1 == Vector(1, 2)
    assert not v1 == v2
