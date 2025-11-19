"""
Найти k-ый по величине элемент массива.
Важно: нельзя просто отсортировать массив. Также не используем кучи, так как про них еще пока не знаем.
Подсказка: quickselect.

Пример:
Ввод: nums = [3,2,1,5,6,4], k = 2
Вывод: 5 (второй по величине элемент)
"""
import random
import time
from typing import List, Callable
from functools import wraps


def measure_time(func: Callable) -> Callable:
    #Декоратор 
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} выполнилась за {end - start:.6f} секунд")
        return result
    return wrapper


def quickselect_kth_largest(nums: List[int], k: int) -> int:
    """
    Находит k-ый по величине (максимальный) элемент используя Quickselect.

    Алгоритм:
    1. Выбираем pivot и разделяем массив на части
    2. Если pivot на позиции k-1 -> ответ
    3. Если k-1 < позиции pivot, ищем в левой части
    4. Иначе ищем в правой части

    Сложность:
    - Средняя O(n), худшая O(n²)
    - Пространственная: O(1) 

    На вход:
        nums: Список чисел
        k: Порядковый номер, k=1 это максимальный элемент

    возвращает k-ый по величине элемент
    """
    if k < 1 or k > len(nums):
        raise ValueError(f"k должно быть от 1 до {len(nums)}, получено: {k}")

    arr = nums.copy()

    # k-ый по величине = (len - k)-ый по возрастанию
    target_index = len(arr) - k

    return quickselect_helper(arr, 0, len(arr) - 1, target_index)


def quickselect_kth_smallest(nums: List[int], k: int) -> int:
    """
     Возвращает k-ый наименьший элемент
    """
    if k < 1 or k > len(nums):
        raise ValueError(f"k должно быть от 1 до {len(nums)}, получено: {k}")

    arr = nums.copy()
    target_index = k - 1  # k-ый элемент находится на индексе k-1

    return quickselect_helper(arr, 0, len(arr) - 1, target_index)


def quickselect_helper(arr: List[int], left: int, right: int, k: int) -> int:
    """
    Вспомогательная рекурсивная функция для Quickselect.

    На вход:
        arr: массив для поиска
        left: левая граница поиска
        right: правая граница поиска
        k: целевой индекс для поиска

    Возвращает элемент на k-ой позиции в отсортированном порядке
    """
    if left == right:
        return arr[left]

    # partition с рандомизацией pivot
    pivot_index = partition_random(arr, left, right)

    # если pivot на нужной позиции - нашли ответ
    if k == pivot_index:
        return arr[k]
    # если k меньше, ищем в левой части
    elif k < pivot_index:
        return quickselect_helper(arr, left, pivot_index - 1, k)
    # иначе ищем в правой части
    else:
        return quickselect_helper(arr, pivot_index + 1, right, k)


def partition_random(arr: List[int], left: int, right: int) -> int:
    """
    Разделение массива с рандомизацией pivot- помогает избежать худшего случая O(n²).
    Возвращает финальную позицию pivot элемента
    """
    # случайный pivot и меняем его с последним
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    pivot = arr[right]
    i = left - 1

    # перемещаем элементы меньше pivot влево
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # ставим pivot на правильное место
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

# Quickselect с медианой медиан (гарантированная O(n))

def quickselect_median_of_medians(nums: List[int], k: int) -> int:

    if k < 1 or k > len(nums):
        raise ValueError(f"k должно быть от 1 до {len(nums)}, получено: {k}")

    arr = nums.copy()
    target_index = len(arr) - k

    return quickselect_mom_helper(arr, 0, len(arr) - 1, target_index)


def quickselect_mom_helper(arr: List[int], left: int, right: int, k: int) -> int:

    if left == right:
        return arr[left]

    # медиана медиан для выбора pivot
    pivot_value = median_of_medians(arr, left, right)

    # индекс этого pivot в массиве
    pivot_index = left
    for i in range(left, right + 1):
        if arr[i] == pivot_value:
            pivot_index = i
            break

    # partition относительно этого pivot
    pivot_index = partition_with_pivot(arr, left, right, pivot_index)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect_mom_helper(arr, left, pivot_index - 1, k)
    else:
        return quickselect_mom_helper(arr, pivot_index + 1, right, k)


def median_of_medians(arr: List[int], left: int, right: int) -> int:
    n = right - left + 1

    # если массив маленький, просто возвращаем медиану
    if n <= 5:
        return sorted(arr[left:right + 1])[n // 2]

    # группы по 5, находим медиану каждой группы
    medians = []
    for i in range(left, right + 1, 5):
        group_right = min(i + 4, right)
        group = sorted(arr[i:group_right + 1])
        median = group[len(group) // 2]
        medians.append(median)

    # рекурсивно находим медиану медиан
    return quickselect_kth_smallest(medians, len(medians) // 2 + 1)


def partition_with_pivot(arr: List[int], left: int, right: int, pivot_index: int) -> int:
    # меняем pivot с последним элементом
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1
