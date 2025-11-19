"""
Тесты для сравнения производительности алгоритмов сортировки.
Запуск: pytest test_compare.py -v -s
"""
import random
import time
import pytest
from compare import merge_sort, quick_sort, quick_sort_inplace


def time_function(func, arr):
    """Измеряет время выполнения функции без декоратора"""
    arr_copy = arr.copy()
    start = time.perf_counter()
    if func == quick_sort_inplace:
        func.__wrapped__(arr_copy)
    else:
        func.__wrapped__(arr_copy)
    end = time.perf_counter()
    return end - start


class TestPerformanceDifferences:
    """Тесты на различных данных, показывающие разницу в производительности"""

    def test_all_identical_elements(self):
        """
        ТЕСТ 1: Все элементы одинаковые

        Ожидание: Quick Sort >> НАМНОГО быстрее
        Причина: все элементы попадают в массив 'equal', рекурсия не нужна - O(n)
        Merge Sort всё равно делит и объединяет - O(n log n)
        """
        print("\n" + "=" * 70)
        print("ТЕСТ 1: Массив с одинаковыми элементами (все = 42)")
        print("=" * 70)

        size = 15000
        arr = [42] * size
        print(f"Размер: {size}")

        time_merge = time_function(merge_sort, arr)
        time_quick = time_function(quick_sort, arr)
        time_quick_inplace = time_function(quick_sort_inplace, arr)

        print(f"  Merge Sort:          {time_merge:.6f} сек")
        print(f"  Quick Sort:          {time_quick:.6f} сек")
        print(f"  Quick Sort in-place: {time_quick_inplace:.6f} сек")

        speedup = time_merge / time_quick
        print(f"\n  Quick Sort быстрее Merge Sort в {speedup:.2f}x раз!")

        # Quick Sort должен быть значительно быстрее
        assert time_quick < time_merge, "Quick Sort должен быть быстрее на одинаковых элементах"

    def test_many_duplicates(self):
        """
        ТЕСТ 2: Много дубликатов (только 10 уникальных значений на 15000 элементов)

        Ожидание: Quick Sort быстрее
        Причина: большой массив 'equal' уменьшает количество рекурсивных вызовов
        """
        print("\n" + "=" * 70)
        print("ТЕСТ 2: Массив с большим количеством дубликатов (10 уникальных значений)")
        print("=" * 70)

        size = 15000
        arr = [random.randint(1, 10) for _ in range(size)]
        print(f"Размер: {size}, уникальных значений: ~10")

        time_merge = time_function(merge_sort, arr)
        time_quick = time_function(quick_sort, arr)
        time_quick_inplace = time_function(quick_sort_inplace, arr)

        print(f"  Merge Sort:          {time_merge:.6f} сек")
        print(f"  Quick Sort:          {time_quick:.6f} сек")
        print(f"  Quick Sort in-place: {time_quick_inplace:.6f} сек")

        speedup = time_merge / time_quick
        print(f"\n  Quick Sort быстрее Merge Sort в {speedup:.2f}x раз!")

    def test_nearly_sorted(self):
        """
        ТЕСТ 3: Почти отсортированный массив (95% уже отсортирован)

        Ожидание: Merge Sort показывает стабильное время, близкое к случайным данным
        Quick Sort может быть чуть медленнее из-за паттерна
        """
        print("\n" + "=" * 70)
        print("ТЕСТ 3: Почти отсортированный массив (95% отсортирован)")
        print("=" * 70)

        size = 10000
        arr = list(range(size))
        # Перемешиваем только 5% элементов
        for _ in range(size // 20):
            i, j = random.randint(0, size - 1), random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]

        print(f"Размер: {size}, перемешано 5% элементов")

        time_merge = time_function(merge_sort, arr)
        time_quick = time_function(quick_sort, arr)
        time_quick_inplace = time_function(quick_sort_inplace, arr)

        print(f"  Merge Sort:          {time_merge:.6f} сек")
        print(f"  Quick Sort:          {time_quick:.6f} сек")
        print(f"  Quick Sort in-place: {time_quick_inplace:.6f} сек")

        ratio = time_merge / time_quick
        print(f"\n  Соотношение времени (Merge/Quick): {ratio:.2f}x")

    def test_sawtooth_pattern(self):
        """
        ТЕСТ 4: Паттерн "пила" (чередуются малые и большие значения)

        Ожидание: Merge Sort стабилен
        Quick Sort может быть медленнее из-за неоптимального разделения
        """
        print("\n" + "=" * 70)
        print("ТЕСТ 4: Паттерн 'пила' (чередование min и max)")
        print("=" * 70)

        size = 8000
        arr = []
        for i in range(size):
            arr.append(i if i % 2 == 0 else size * 2 - i)

        print(f"Размер: {size}, паттерн: [0, {size*2-1}, 2, {size*2-3}, ...]")

        time_merge = time_function(merge_sort, arr)
        time_quick = time_function(quick_sort, arr)
        time_quick_inplace = time_function(quick_sort_inplace, arr)

        print(f"  Merge Sort:          {time_merge:.6f} сек")
        print(f"  Quick Sort:          {time_quick:.6f} сек")
        print(f"  Quick Sort in-place: {time_quick_inplace:.6f} сек")

        ratio = time_merge / time_quick
        print(f"\n  Соотношение времени (Merge/Quick): {ratio:.2f}x")

    def test_narrow_range(self):
        """
        ТЕСТ 5: Большой массив с узким диапазоном значений (1-100)

        Ожидание: Quick Sort быстрее из-за множества дубликатов
        """
        print("\n" + "=" * 70)
        print("ТЕСТ 5: Большой массив, узкий диапазон значений (1-100)")
        print("=" * 70)

        size = 20000
        arr = [random.randint(1, 100) for _ in range(size)]
        print(f"Размер: {size}, диапазон: 1-100")

        time_merge = time_function(merge_sort, arr)
        time_quick = time_function(quick_sort, arr)
        time_quick_inplace = time_function(quick_sort_inplace, arr)

        print(f"  Merge Sort:          {time_merge:.6f} сек")
        print(f"  Quick Sort:          {time_quick:.6f} сек")
        print(f"  Quick Sort in-place: {time_quick_inplace:.6f} сек")

        speedup = time_merge / time_quick
        print(f"\n  Quick Sort быстрее Merge Sort в {speedup:.2f}x раз!")

    def test_descending_steps(self):
        """
        ТЕСТ 6: Убывающие "ступени" (блоки одинаковых значений)

        Ожидание: Quick Sort значительно быстрее
        Причина: каждый блок одинаковых значений обрабатывается за O(n)
        """
        print("\n" + "=" * 70)
        print("ТЕСТ 6: Убывающие 'ступени' (блоки одинаковых значений)")
        print("=" * 70)

        arr = []
        for i in range(100, 0, -1):
            arr.extend([i] * 100)

        size = len(arr)
        print(f"Размер: {size}, структура: [100]*100 + [99]*100 + ... + [1]*100")

        time_merge = time_function(merge_sort, arr)
        time_quick = time_function(quick_sort, arr)
        time_quick_inplace = time_function(quick_sort_inplace, arr)

        print(f"  Merge Sort:          {time_merge:.6f} сек")
        print(f"  Quick Sort:          {time_quick:.6f} сек")
        print(f"  Quick Sort in-place: {time_quick_inplace:.6f} сек")

        speedup = time_merge / time_quick
        print(f"\n  Quick Sort быстрее Merge Sort в {speedup:.2f}x раз!")

    def test_random_uniform(self):
        """
        ТЕСТ 7: Равномерное случайное распределение (базовый случай для сравнения)

        Ожидание: Похожая производительность, оба O(n log n)
        Обычно Quick Sort немного быстрее из-за меньших констант
        """
        print("\n" + "=" * 70)
        print("ТЕСТ 7: Равномерное случайное распределение (BASELINE)")
        print("=" * 70)

        size = 15000
        arr = [random.randint(1, 100000) for _ in range(size)]
        print(f"Размер: {size}, диапазон: 1-100000 (уникальные значения)")

        time_merge = time_function(merge_sort, arr)
        time_quick = time_function(quick_sort, arr)
        time_quick_inplace = time_function(quick_sort_inplace, arr)

        print(f"  Merge Sort:          {time_merge:.6f} сек")
        print(f"  Quick Sort:          {time_quick:.6f} сек")
        print(f"  Quick Sort in-place: {time_quick_inplace:.6f} сек")

        ratio = time_merge / time_quick
        print(f"\n  Соотношение времени (Merge/Quick): {ratio:.2f}x")

    def test_alternating_duplicates(self):
        """
        ТЕСТ 8: Чередование двух значений [1,2,1,2,1,2,...]

        Ожидание: Quick Sort НАМНОГО быстрее
        Причина: только два уникальных значения, минимальная рекурсия
        """
        print("\n" + "=" * 70)
        print("ТЕСТ 8: Чередование двух значений [1,2,1,2,1,2,...]")
        print("=" * 70)

        size = 15000
        arr = [1 if i % 2 == 0 else 2 for i in range(size)]
        print(f"Размер: {size}, только 2 уникальных значения")

        time_merge = time_function(merge_sort, arr)
        time_quick = time_function(quick_sort, arr)
        time_quick_inplace = time_function(quick_sort_inplace, arr)

        print(f"  Merge Sort:          {time_merge:.6f} сек")
        print(f"  Quick Sort:          {time_quick:.6f} сек")
        print(f"  Quick Sort in-place: {time_quick_inplace:.6f} sek")

        speedup = time_merge / time_quick
        print(f"\n  Quick Sort быстрее Merge Sort в {speedup:.2f}x раз!")

        # Quick Sort должен быть значительно быстрее
        assert time_quick < time_merge * 0.8, "Quick Sort должен быть быстрее на двух значениях"


class TestCorrectness:
    """Тесты корректности сортировки"""

    def test_correctness_random(self):
        """Проверка корректности на случайных данных"""
        arr = [random.randint(1, 1000) for _ in range(1000)]
        expected = sorted(arr)

        assert merge_sort.__wrapped__(arr.copy()) == expected
        assert quick_sort.__wrapped__(arr.copy()) == expected

        arr_copy = arr.copy()
        quick_sort_inplace.__wrapped__(arr_copy)
        assert arr_copy == expected

    def test_correctness_duplicates(self):
        """Проверка корректности на данных с дубликатами"""
        arr = [random.randint(1, 10) for _ in range(1000)]
        expected = sorted(arr)

        assert merge_sort.__wrapped__(arr.copy()) == expected
        assert quick_sort.__wrapped__(arr.copy()) == expected

        arr_copy = arr.copy()
        quick_sort_inplace.__wrapped__(arr_copy)
        assert arr_copy == expected

    def test_correctness_edge_cases(self):
        """Проверка корректности на граничных случаях"""
        test_cases = [
            [],
            [1],
            [2, 1],
            [1, 2, 3],
            [3, 2, 1],
            [1, 1, 1],
        ]

        for arr in test_cases:
            expected = sorted(arr)
            assert merge_sort.__wrapped__(arr.copy()) == expected
            assert quick_sort.__wrapped__(arr.copy()) == expected

            arr_copy = arr.copy()
            quick_sort_inplace.__wrapped__(arr_copy)
            assert arr_copy == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
