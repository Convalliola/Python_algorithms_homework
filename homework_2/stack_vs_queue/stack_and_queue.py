class Node:
    """Узел связного списка"""
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """LIFO - Last In First Out на основе связного списка"""

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "Stack: []"
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return f"Stack: [{' -> '.join(elements)}] (top -> bottom)"


class Queue:
    """FIFO - First In First Out на основе связного списка"""

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.front.data

    def is_empty(self):
        """Проверить, пуста ли очередь"""
        return self.front is None

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        return f"Queue: [{' -> '.join(elements)}] (front -> rear)"
