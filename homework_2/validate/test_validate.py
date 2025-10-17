import pytest

from validate_stack_sequences import validate_stack_sequences

#пример из условия
@pytest.mark.parametrize(
    "pushed,popped,expected",
    [
        ([1, 2, 3, 4, 5], [1, 3, 5, 4, 2], True),  #  True
        ([1, 2, 3], [3, 1, 2], False),  #  False
    ],
)
def test_examples(pushed, popped, expected):
    assert validate_stack_sequences(pushed, popped) is expected


@pytest.mark.parametrize(
    "pushed,popped",
    [
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),  # мгновенный pop после каждого push
        ([1, 2, 3], [2, 1, 3]),  # допустимая последовательность
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # сначала все push, потом все pop
        ([2, 1, 0], [1, 2, 0]),
        ([0, 2, 1], [0, 1, 2]),
    ],
)
def test_valid_sequences(pushed, popped):
    assert validate_stack_sequences(pushed, popped) is True


@pytest.mark.parametrize(
    "pushed,popped",
    [
        ([1, 2, 3], [3, 1, 2]),  # из условия невозможно
        ([1, 2, 3, 4], [4, 1, 3, 2]),  # потребовался бы pop(1) при вершине 3
    ],
)
def test_invalid_sequences(pushed, popped):
    assert validate_stack_sequences(pushed, popped) is False


def test_length_mismatch():
    assert validate_stack_sequences([1, 2, 3], [1, 2]) is False


def test_large_case_reverse_order():
    n = 100_000
    pushed = list(range(1, n + 1))
    popped = list(range(n, 1 - 1, -1))
    assert validate_stack_sequences(pushed, popped) is True


