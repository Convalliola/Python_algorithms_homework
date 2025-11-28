"""
Найти k-ый по величине элемент массива. Важно: нельзя просто отсортировать массив. Для решения необходимо использовать minheap. 
На выходе должно быть две реализции:

1) без использования heapq (кучу и методы работы с ней реализовываем сами)

2) с использованием heapq 

Пример:
Вход: nums = [3,2,1,5,6,4], k = 2
Выход: 5 (2-й наибольший элемент)
"""

import heapq

class MinHeap:
    """
    Кастомная реализация Min-Heap
    """

    def __init__(self):
        self.heap = []

    def size(self):
        # возвращает размер кучи
        return len(self.heap)

    def peek(self):
        # получить минимальный элемент без удаления
        if not self.heap:
            return None
        return self.heap[0]

    def push(self, value):
        # вставить элемент в кучу
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        # удалить и вернуть минимальный элемент
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # меняем корень с последним элементом
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)

        return min_val

    def _sift_up(self, index):
        # просеивание элемента вверх для поддержания свойств кучи
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = \
                    self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _sift_down(self, index):
        # просеивание элемента вниз для поддержания свойств кучи
        n = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = \
                    self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


def find_kth_largest_custom(nums, k):
    """
    Найти k-ый наибольший элемент используя кастомную min-heap.

    Алгоритм:
    1. Поддерживаем min-heap размера k
    2. Для каждого элемента в nums:
       - Если размер кучи < k: добавить элемент
       - Если элемент > минимума кучи: удалить минимум, добавить элемент
    3. Вернуть минимум кучи (k-ый наибольший)

    Временная сложность: O(N log k)
    Пространственная сложность: O(k)
    """
    if not nums or k <= 0 or k > len(nums):
        raise ValueError("Некорректный ввод")

    heap = MinHeap()

    for num in nums:
        if heap.size() < k:
            # куча еще не заполнена, добавляем элемент
            heap.push(num)
        elif num > heap.peek():
            # нашли больший элемент, заменяем наименьший
            heap.pop()
            heap.push(num)

    # корень min-heap это k-ый наибольший
    return heap.peek()


# РЕАЛИЗАЦИЯ 2: с использованием библиотеки heapq


def find_kth_largest_heapq(nums, k):
    """
    Временная сложность: O(N log k)
    Пространственная сложность: O(k)
    """
    if not nums or k <= 0 or k > len(nums):
        raise ValueError("Некорректный ввод")

    # heapq использует список как min-heap
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)

    # Корень кучи это k-ый наибольший
    return heap[0]
    
    
# АЛЬТЕРНАТИВНЫЙ ПОДХОД: использование nsmallest/nlargest

def find_kth_largest_heapq_simple(nums, k):

    if not nums or k <= 0 or k > len(nums):
        raise ValueError("Некорректный ввод")

    return heapq.nlargest(k, nums)[k - 1]
