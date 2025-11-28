import time
import random


def sift_up(heap, index):
    """
    Просеивание элемента вверх (для метода O(N log N))
    """
    while index > 0:
        parent_index = (index - 1) // 2
        if heap[index] < heap[parent_index]:
            heap[index], heap[parent_index] = heap[parent_index], heap[index]
            index = parent_index
        else:
            break


def sift_down(heap, index, heap_size):
    """
    Просеивание элемента вниз (для метода O(N))
    """
    while True:
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < heap_size and heap[left_child] < heap[smallest]:
            smallest = left_child

        if right_child < heap_size and heap[right_child] < heap[smallest]:
            smallest = right_child

        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest
        else:
            break


def makeheap_n_log_n(arr):
    """
    Построение min-heap за O(N log N).

    Алгоритм:
    1. Создаём пустую кучу
    2. Последовательно вставляем каждый элемент из массива
    3. После каждой вставки просеиваем элемент вверх (sift_up)

    Сложность: O(N log N), где N - количество элементов
    - N вставок
    - Каждая вставка требует O(log N) операций просеивания вверх
    """
    heap = []
    for element in arr:
        heap.append(element)
        sift_up(heap, len(heap) - 1)
    return heap


def makeheap(arr):
    """
    Построение min-heap за O(N) (метод "кучи снизу вверх")

    Алгоритм:
    1. Копируем массив
    2. Начинаем с последнего не-листового узла (индекс n//2 - 1)
    3. Применяем sift_down для каждого узла, двигаясь к корню

    Сложность: O(N), где N - количество элементов
    - Хотя каждый sift_down может быть O(log N), большинство узлов
      находятся внизу дерева и требуют мало операций
    """
    if not arr:
        return []

    heap = arr.copy()
    n = len(heap)

    # Начинаем с последнего не-листового узла и движемся к корню
    for i in range(n // 2 - 1, -1, -1):
        sift_down(heap, i, n)

    return heap


def is_min_heap(arr):
    """
    Проверка, является ли массив корректной min-heap
    """
    n = len(arr)
    for i in range(n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[i] > arr[left_child]:
            return False
        if right_child < n and arr[i] > arr[right_child]:
            return False

    return True


def compare_performance():
    """
    Сравнение производительности двух методов
    """
    sizes = [100, 1000, 5000, 10000, 20000]

    print("СРАВНЕНИЕ МЕТОДОВ")
    print("-" * 60)

    for size in sizes:
        # Генерируем случайный массив
        arr = [random.randint(1, 100000) for _ in range(size)]

        # Измеряем время для метода O(N log N)
        arr_copy = arr.copy()
        start = time.perf_counter()
        heap1 = makeheap_n_log_n(arr_copy)
        time_n_log_n = time.perf_counter() - start

        # Измеряем время для метода O(N)
        arr_copy = arr.copy()
        start = time.perf_counter()
        heap2 = makeheap(arr_copy)
        time_n = time.perf_counter() - start

        # Проверяем корректность
        assert is_min_heap(heap1), f"makeheap_n_log_n создала некорректную heap для размера {size}"
        assert is_min_heap(heap2), f"makeheap создала некорректную heap для размера {size}"

        ratio = time_n_log_n / time_n if time_n > 0 else 0
        if size == 1000:
            ratio1=ratio
        print(f'Size: {size}   O(N log N): {time_n_log_n*1000:.4f}  O(N): {time_n*1000:.4f}  ratio: {ratio:.4f}')
    
    print(f"\nНа {sizes[1]} элементах алгоритм за O(N) быстрее в {ratio1} раз")
    print(f"На {sizes[-1]} элементах алгоритм за O(N) быстрее в {ratio} раз")
    print("\nВремя указано в миллисекундах")

if __name__ == "__main__":
    # Сравниваем производительность
    compare_performance()
