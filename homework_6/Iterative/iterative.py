"""
Реализовать итеративные версии mergesort и quicksort.
"""
import time
from functools import wraps
from typing import List, Callable, Any


def measure_time(func: Callable) -> Callable:
    """
    Декоратор для замера времени выполнения функции.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"{func.__name__} выполнилась за {execution_time:.6f} секунд")
        return result
    return wrapper


@measure_time
def merge_sort_iterative(arr: List[int]) -> List[int]:
    """
    Итеративная реализация Merge Sort.

    Алгоритм:
    1. Начинаем с размера блока 1
    2. Постепенно увеличиваем размер блока (1, 2, 4, 8, ...)
    3. На каждом шаге сливаем соседние блоки текущего размера
    4. Продолжаем до тех пор, пока размер блока не превысит размер массива

    Сложность:
    Время: O(n log n)
    Память: O(n) для временного массива
    """
    if len(arr) <= 1:
        return arr

    result = arr.copy()
    n = len(result)

    # начинаем с блоков размера 1, затем удваиваем размер
    current_size = 1

    while current_size < n:
        # начинаем с левого края массива
        left_start = 0

        while left_start < n:
            # находим конец левого блока
            left_end = min(left_start + current_size - 1, n - 1)

            # находим конец правого блока
            right_end = min(left_start + 2 * current_size - 1, n - 1)

            # если есть правый блок для слияния
            if left_end < right_end:
                merge_inplace(result, left_start, left_end, right_end)

            # переходим к следующей паре блоков
            left_start += 2 * current_size

        # увеличиваем размер блока в два раза
        current_size *= 2

    return result


def merge_inplace(arr: List[int], left: int, mid: int, right: int) -> None:
    """
    Вспомогательная функция для слияния двух соседних отсортированных блоков.

    На вход:
        arr: Массив для слияния
        left: Начальный индекс левого блока
        mid: Конечный индекс левого блока
        right: Конечный индекс правого блока
    """
    # временные массивы для левой и правой частей
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0  # индекс для левой части
    j = 0  # индекс для правой части
    k = left  # индекс для результирующего массива

    # сливаем два массива
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # копируем оставшиеся элементы из левой части
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    # копируем оставшиеся элементы из правой части
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


@measure_time
def quick_sort_iterative(arr: List[int]) -> List[int]:
    """
    Итеративная реализация Quick Sort.

    Алгоритм:
    1. Используем стек для хранения границ подмассивов
    2. Извлекаем границы из стека
    3. Выполняем разделение (partition)
    4. Добавляем границы левой и правой частей в стек
    5. Повторяем до тех пор, пока стек не опустеет

    Сложность:
    - Время: O(n log n) в среднем, O(n²) в худшем случае
    - память: O(log n) для стека
    """
    if len(arr) <= 1:
        return arr

    result = arr.copy()

    # стек для хранения границ подмассивов
    # Каждый элемент стека это кортеж (low, high)
    stack = [(0, len(result) - 1)]

    while stack:
        # извлекаем границы подмассива из стека
        low, high = stack.pop()

        if low < high:
            # выполняем разделение и получаем индекс pivot
            pivot_index = partition(result, low, high)

            # добавляем левую часть в стек если существует
            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))

            # добавляем правую часть в стек 
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))

    return result


@measure_time
def quick_sort_iterative_optimized(arr: List[int]) -> List[int]:
    """
    Оптимизированная итеративная реализация быстрой сортировки.
    1. Обрабатываем меньший подмассив (для ограничения размера стека до O(log n))
    2. Используем трехстороннее разделение для эффективной обработки дубликатов
    3. Рандомизация pivot для избежания худшего случая
    """
    if len(arr) <= 1:
        return arr

    result = arr.copy()
    stack = [(0, len(result) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            # используем трехстороннее разделение
            lt, gt = three_way_partition_iterative(result, low, high)

            # определяем размеры левой и правой частей
            left_size = lt - low
            right_size = high - gt

            # сначала помещаем в стек большую часть, затем меньшую
            if left_size > right_size:
                if lt - 1 > low:
                    stack.append((low, lt - 1))
                if gt + 1 < high:
                    stack.append((gt + 1, high))
            else:
                if gt + 1 < high:
                    stack.append((gt + 1, high))
                if lt - 1 > low:
                    stack.append((low, lt - 1))

    return result


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Стандартное разделение массива относительно опорного элемента.
    Возвращает индекс опорного элемента после разделения
    """
    import random

    # выбираем случайный pivot и меняем его с последним
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def three_way_partition_iterative(arr: List[int], low: int, high: int) -> tuple:
    """
    Трехстороннее разделение
    """
    import random

    # выбираем случайный pivot и перемещаем его в начало
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    pivot = arr[low]
    lt = low
    i = low + 1
    gt = high

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    return lt, gt
