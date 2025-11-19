"""
Реализовать рекурсивные версии mergesort и quicksort.
Реализовать декоратор, который будет замерять время выполнения функции.
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
def merge_sort(arr: List[int]) -> List[int]:
    """
    Рекурсивная реализация сортировки Merge Sort.

    Алгоритм:
    1. Разделить массив на две половины
    2. Рекурсивно отсортировать каждую половину
    3. Слить две отсортированные половины

    Сложность:
    - время: O(n log n) 
    - память: O(n)
    """
    # базовый случай когда массив из 0 или 1 элемента уже отсортирован
    if len(arr) <= 1:
        return arr

    # делим массив на две половины
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # рекурсивно сортируем каждую половину
    left = merge_sort.__wrapped__(left)  # Используем __wrapped__ чтобы избежать повторного замера времени
    right = merge_sort.__wrapped__(right)

    # сливаем отсортированные половины
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    функция для слияния двух отсортированных массивов.

    На вход:
        left - первый отсортированный массив
        right - второй 

    Возвращает объединённый отсортированный массив
    """
    result = []
    i = j = 0

    # сравниваем элементы из обоих массивов и добавляем меньший
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])

    return result


@measure_time
def quick_sort(arr: List[int]) -> List[int]:
    """
    рекурсивная реализация Quick Sort.

    Алгоритм:
    1. Выбрать опорный элемент (pivot)
    2. Разделить массив на три части: меньше pivot, равные pivot, больше pivot
    3. Рекурсивно отсортировать части меньше и больше pivot
    4. Объединить результаты

    Сложность:
    время: O(n log n), в худшем случае - O(n²) 
    память: O(log n) для стека рекурсии
    """
    # массив из 0 или 1 элемента уже отсортирован
    if len(arr) <= 1:
        return arr

    # опорный элемент (pivot) - средний элемент
    pivot = arr[len(arr) // 2]

    # делим массив на три части
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Рекурсивно сортируем части и объединяем
    # Используем __wrapped__ чтобы избежать повторного замера времени
    return quick_sort.__wrapped__(less) + equal + quick_sort.__wrapped__(greater)


@measure_time
def quick_sort_inplace(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    """
    Рекурсивная реализация быстрой сортировки на месте.
    Использует трехстороннее разделение (Dutch National Flag) для эффективной
    обработки дубликатов.

    На вход:
        arr: Список для сортировки
        low: Начальный индекс
        high: Конечный индекс

    Возвращает:
        Отсортированный список (модифицирует исходный список)
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # трехстороннее разделение возвращает границы секции с равными элементами
        lt, gt = three_way_partition(arr, low, high)

        # рекурсивно сортируем части меньше и больше pivot
        # элементы равные pivot уже на своих местах
        quick_sort_inplace.__wrapped__(arr, low, lt - 1)
        quick_sort_inplace.__wrapped__(arr, gt + 1, high)

    return arr


def three_way_partition(arr: List[int], low: int, high: int) -> tuple:
    """
    Трехстороннее разделение
    Делит массив на три части: < pivot, == pivot, > pivot

    эффективно для массивов с большим количеством дубликатов,
    так как элементы равные pivot не участвуют в рекурсии.

    возвращает:
        Кортеж (lt, gt) где:
        - arr[low..lt-1] < pivot
        - arr[lt..gt] == pivot
        - arr[gt+1..high] > pivot
    """
    import random

    # выбираем случайный pivot и перемещаем его в начало
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    pivot = arr[low]
    lt = low       # граница элементов < pivot
    i = low + 1    # текущий элемент
    gt = high      # граница элементов > pivot

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:  # arr[i] == pivot
            i += 1

    return lt, gt


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Стандартное разделение 
    Использует рандомизацию для выбора pivot.
    Возвращает индекс опорного элемента после разделения
    """
    import random

    # выбираем случайный элемент как опорный и меняем его с последним
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    # перемещаем элементы меньше pivot влево
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # ставим pivot на правильное место
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
