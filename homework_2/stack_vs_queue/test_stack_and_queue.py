import pytest
from stack_and_queue import Stack, Queue


class TestStack:

    def test_stack_initialization(self):
        stack = Stack()
        assert stack.is_empty() is True
        assert len(stack) == 0

    def test_push_single_element(self):
        stack = Stack()
        stack.push(1)
        assert stack.is_empty() is False
        assert len(stack) == 1
        assert stack.peek() == 1

    def test_push_multiple_elements(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert len(stack) == 3
        assert stack.peek() == 3

    def test_pop_single_element(self):
        stack = Stack()
        stack.push(1)
        value = stack.pop()
        assert value == 1
        assert stack.is_empty() is True
        assert len(stack) == 0

    def test_pop_multiple_elements(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty() is True

    def test_pop_empty_stack(self):
        stack = Stack()
        with pytest.raises(IndexError, match="Стек пуст"):
            stack.pop()

    def test_peek_empty_stack(self):
        stack = Stack()
        with pytest.raises(IndexError, match="Стек пуст"):
            stack.peek()

    def test_peek_does_not_remove_element(self):
        stack = Stack()
        stack.push(1)
        assert stack.peek() == 1
        assert len(stack) == 1
        assert stack.peek() == 1

    def test_push_pop_sequence(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 1

    def test_stack_with_different_types(self):
        stack = Stack()
        stack.push(1)
        stack.push("string")
        stack.push([1, 2, 3])
        stack.push({"key": "value"})
        assert stack.pop() == {"key": "value"}
        assert stack.pop() == [1, 2, 3]
        assert stack.pop() == "string"
        assert stack.pop() == 1

    def test_stack_str_representation(self):
        stack = Stack()
        assert "[]" in str(stack)
        stack.push(1)
        stack.push(2)
        assert "1" in str(stack)
        assert "2" in str(stack)


class TestQueue:
    """Тесты для Queue"""

    def test_queue_initialization(self):
        queue = Queue()
        assert queue.is_empty() is True
        assert len(queue) == 0

    def test_enqueue_single_element(self):
        queue = Queue()
        queue.enqueue(1)
        assert queue.is_empty() is False
        assert len(queue) == 1
        assert queue.peek() == 1

    def test_enqueue_multiple_elements(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert len(queue) == 3
        assert queue.peek() == 1

    def test_dequeue_single_element(self):
        queue = Queue()
        queue.enqueue(1)
        value = queue.dequeue()
        assert value == 1
        assert queue.is_empty() is True
        assert len(queue) == 0

    def test_dequeue_multiple_elements(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.is_empty() is True

    def test_dequeue_empty_queue(self):
        queue = Queue()
        with pytest.raises(IndexError, match="Очередь пуста"):
            queue.dequeue()

    def test_peek_empty_queue(self):
        queue = Queue()
        with pytest.raises(IndexError, match="Очередь пуста"):
            queue.peek()

    def test_peek_does_not_remove_element(self):
        queue = Queue()
        queue.enqueue(1)
        assert queue.peek() == 1
        assert len(queue) == 1
        assert queue.peek() == 1

    def test_enqueue_dequeue_sequence(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        queue.enqueue(3)
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3

    def test_queue_with_different_types(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue("string")
        queue.enqueue([1, 2, 3])
        queue.enqueue({"key": "value"})
        assert queue.dequeue() == 1
        assert queue.dequeue() == "string"
        assert queue.dequeue() == [1, 2, 3]
        assert queue.dequeue() == {"key": "value"}

    def test_queue_str_representation(self):
        queue = Queue()
        assert "[]" in str(queue)
        queue.enqueue(1)
        queue.enqueue(2)
        assert "1" in str(queue)
        assert "2" in str(queue)

    def test_queue_maintains_order(self):
        queue = Queue()
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            queue.enqueue(elem)
        for elem in elements:
            assert queue.dequeue() == elem


class TestStackEdgeCases:
    """Тесты пограничных случаев для стека"""

    def test_stack_large_number_of_elements(self):
        """Тест стека с большим количеством элементов"""
        stack = Stack()
        n = 1000
        for i in range(n):
            stack.push(i)
        assert len(stack) == n
        for i in range(n - 1, -1, -1):
            assert stack.pop() == i

    def test_stack_push_none(self):
        """Тест добавления None в стек"""
        stack = Stack()
        stack.push(None)
        assert stack.peek() is None
        assert stack.pop() is None


class TestQueueEdgeCases:
    """Тесты граничных случаев для очереди"""

    def test_queue_large_number_of_elements(self):
        """Тест очереди с большим количеством элементов"""
        queue = Queue()
        n = 1000
        for i in range(n):
            queue.enqueue(i)
        assert len(queue) == n
        for i in range(n):
            assert queue.dequeue() == i

    def test_queue_enqueue_none(self):
        """Тест добавления None в очередь"""
        queue = Queue()
        queue.enqueue(None)
        assert queue.peek() is None
        assert queue.dequeue() is None

    def test_queue_single_element_front_rear(self):
        """Тест что front и rear указывают на один элемент"""
        queue = Queue()
        queue.enqueue(1)
        assert queue.dequeue() == 1
        assert queue.is_empty() is True
