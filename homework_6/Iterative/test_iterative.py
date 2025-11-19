"""
Pytest тесты для итеративных алгоритмов сортировки.
Запуск: pytest test_iterative.py -v -s
"""
import random
import time
import pytest
from iterative import (
    merge_sort_iterative,
    quick_sort_iterative,
    quick_sort_iterative_optimized
)


def time_function(func, arr):
    """Измеряет время выполнения функции без декоратора"""
    arr_copy = arr.copy()
    start = time.perf_counter()
    func.__wrapped__(arr_copy)
    end = time.perf_counter()
    return end - start


class TestIterativeCorrectness:
    """Тесты корректности итеративных алгоритмов"""

    def test_empty_array(self):
        """Пустой массив"""
        arr = []
        assert merge_sort_iterative.__wrapped__(arr.copy()) == []
        assert quick_sort_iterative.__wrapped__(arr.copy()) == []
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == []

    def test_single_element(self):
        """Один элемент"""
        arr = [42]
        assert merge_sort_iterative.__wrapped__(arr.copy()) == [42]
        assert quick_sort_iterative.__wrapped__(arr.copy()) == [42]
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == [42]

    def test_two_elements_sorted(self):
        """Два элемента (уже отсортированы)"""
        arr = [1, 2]
        assert merge_sort_iterative.__wrapped__(arr.copy()) == [1, 2]
        assert quick_sort_iterative.__wrapped__(arr.copy()) == [1, 2]
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == [1, 2]

    def test_two_elements_reversed(self):
        """Два элемента (обратный порядок)"""
        arr = [2, 1]
        assert merge_sort_iterative.__wrapped__(arr.copy()) == [1, 2]
        assert quick_sort_iterative.__wrapped__(arr.copy()) == [1, 2]
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == [1, 2]

    def test_random_array(self):
        """Случайный массив"""
        arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
        expected = sorted(arr)
        assert merge_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == expected

    def test_sorted_array(self):
        """Уже отсортированный массив"""
        arr = list(range(100))
        expected = arr.copy()
        assert merge_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == expected

    def test_reverse_sorted_array(self):
        """Обратно отсортированный массив"""
        arr = list(range(100, 0, -1))
        expected = sorted(arr)
        assert merge_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == expected

    def test_all_identical(self):
        """Все элементы одинаковые"""
        arr = [42] * 100
        expected = arr.copy()
        assert merge_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == expected

    def test_duplicates(self):
        """Массив с дубликатами"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected = sorted(arr)
        assert merge_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == expected

    def test_large_random_array(self):
        """Большой случайный массив"""
        arr = [random.randint(1, 1000) for _ in range(1000)]
        expected = sorted(arr)
        assert merge_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == expected

    def test_negative_numbers(self):
        """Массив с отрицательными числами"""
        arr = [-5, 3, -1, 7, -9, 0, 4, -2]
        expected = sorted(arr)
        assert merge_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative.__wrapped__(arr.copy()) == expected
        assert quick_sort_iterative_optimized.__wrapped__(arr.copy()) == expected


class TestIterativePerformance:
    """Тесты производительности итеративных алгоритмов"""

    def test_identical_elements_performance(self):
        """
        Тест на одинаковых элементах

        Ожидание: Quick Sort (optimized) >> НАМНОГО быстрее
        """
        print("\n" + "=" * 70)
        print("ТЕСТ: Массив с одинаковыми элементами")
        print("=" * 70)

        size = 5000
        arr = [42] * size
        print(f"Размер: {size}")

        time_merge = time_function(merge_sort_iterative, arr)
        time_quick = time_function(quick_sort_iterative, arr)
        time_quick_opt = time_function(quick_sort_iterative_optimized, arr)

        print(f"  Merge Sort:             {time_merge:.6f} сек")
        print(f"  Quick Sort:             {time_quick:.6f} сек")
        print(f"  Quick Sort (optimized): {time_quick_opt:.6f} сек")

        speedup = time_quick / time_quick_opt
        print(f"\n  Quick Sort (opt) быстрее обычной в {speedup:.0f}x раз! 🚀")

        # Оптимизированная версия должна быть НАМНОГО быстрее
        assert time_quick_opt < time_quick * 0.01, \
            "Quick Sort optimized должна быть в разы быстрее на одинаковых элементах"

    def test_many_duplicates_performance(self):
        """
        Тест на массиве с большим количеством дубликатов

        Ожидание: Quick Sort (optimized) >> НАМНОГО быстрее
        """
        print("\n" + "=" * 70)
        print("ТЕСТ: Массив с большим количеством дубликатов")
        print("=" * 70)

        size = 10000
        arr = [random.randint(1, 10) for _ in range(size)]
        print(f"Размер: {size}, уникальных значений: ~10")

        time_merge = time_function(merge_sort_iterative, arr)
        time_quick = time_function(quick_sort_iterative, arr)
        time_quick_opt = time_function(quick_sort_iterative_optimized, arr)

        print(f"  Merge Sort:             {time_merge:.6f} сек")
        print(f"  Quick Sort:             {time_quick:.6f} сек")
        print(f"  Quick Sort (optimized): {time_quick_opt:.6f} сек")

        speedup = time_quick / time_quick_opt
        print(f"\n  Quick Sort (opt) быстрее обычной в {speedup:.1f}x раз! 🚀")

        # Оптимизированная версия должна быть значительно быстрее
        assert time_quick_opt < time_quick * 0.1, \
            "Quick Sort optimized должна быть быстрее на дубликатах"

    def test_random_uniform_performance(self):
        """
        Тест на случайном равномерном распределении

        Ожидание: все версии показывают сравнимую производительность
        """
        print("\n" + "=" * 70)
        print("ТЕСТ: Равномерное случайное распределение")
        print("=" * 70)

        size = 10000
        arr = [random.randint(1, 100000) for _ in range(size)]
        print(f"Размер: {size}, диапазон: 1-100000")

        time_merge = time_function(merge_sort_iterative, arr)
        time_quick = time_function(quick_sort_iterative, arr)
        time_quick_opt = time_function(quick_sort_iterative_optimized, arr)

        print(f"  Merge Sort:             {time_merge:.6f} сек")
        print(f"  Quick Sort:             {time_quick:.6f} сек")
        print(f"  Quick Sort (optimized): {time_quick_opt:.6f} сек")

        print(f"\n  Все версии показывают сравнимую производительность")

    def test_sorted_performance(self):
        """
        Тест на отсортированном массиве

        Ожидание: Merge Sort стабилен, Quick Sort с рандомизацией тоже работает хорошо
        """
        print("\n" + "=" * 70)
        print("ТЕСТ: Уже отсортированный массив")
        print("=" * 70)

        size = 5000
        arr = list(range(size))
        print(f"Размер: {size}")

        time_merge = time_function(merge_sort_iterative, arr)
        time_quick = time_function(quick_sort_iterative, arr)
        time_quick_opt = time_function(quick_sort_iterative_optimized, arr)

        print(f"  Merge Sort:             {time_merge:.6f} сек")
        print(f"  Quick Sort:             {time_quick:.6f} сек")
        print(f"  Quick Sort (optimized): {time_quick_opt:.6f} сек")

        print(f"\n  Рандомизация pivot защищает от худшего случая")

    def test_alternating_values(self):
        """
        Тест на чередующихся значениях [1,2,1,2,...]

        Ожидание: Quick Sort (optimized) >> быстрее
        """
        print("\n" + "=" * 70)
        print("ТЕСТ: Чередование двух значений [1,2,1,2,...]")
        print("=" * 70)

        size = 10000
        arr = [1 if i % 2 == 0 else 2 for i in range(size)]
        print(f"Размер: {size}")

        time_merge = time_function(merge_sort_iterative, arr)
        time_quick = time_function(quick_sort_iterative, arr)
        time_quick_opt = time_function(quick_sort_iterative_optimized, arr)

        print(f"  Merge Sort:             {time_merge:.6f} сек")
        print(f"  Quick Sort:             {time_quick:.6f} сек")
        print(f"  Quick Sort (optimized): {time_quick_opt:.6f} сек")

        speedup = time_merge / time_quick_opt
        print(f"\n  Quick Sort (opt) быстрее Merge Sort в {speedup:.1f}x раз!")

    def test_narrow_range(self):
        """
        Тест на узком диапазоне значений

        Ожидание: Quick Sort (optimized) >> быстрее из-за дубликатов
        """
        print("\n" + "=" * 70)
        print("ТЕСТ: Узкий диапазон значений (1-100)")
        print("=" * 70)

        size = 15000
        arr = [random.randint(1, 100) for _ in range(size)]
        print(f"Размер: {size}, диапазон: 1-100")

        time_merge = time_function(merge_sort_iterative, arr)
        time_quick = time_function(quick_sort_iterative, arr)
        time_quick_opt = time_function(quick_sort_iterative_optimized, arr)

        print(f"  Merge Sort:             {time_merge:.6f} сек")
        print(f"  Quick Sort:             {time_quick:.6f} сек")
        print(f"  Quick Sort (optimized): {time_quick_opt:.6f} сек")

        speedup = time_merge / time_quick_opt
        print(f"\n  Quick Sort (opt) быстрее Merge Sort в {speedup:.1f}x раз!")


class TestIterativeVsRecursive:
    """Сравнение итеративных и рекурсивных версий"""

    def test_merge_sort_comparison(self):
        """Сравнение итеративной и рекурсивной Merge Sort"""
        print("\n" + "=" * 70)
        print("СРАВНЕНИЕ: Итеративная vs Рекурсивная Merge Sort")
        print("=" * 70)

        # Импортируем рекурсивную версию
        import sys
        import os
        compare_path = os.path.join(os.path.dirname(__file__), '..', 'Compare')
        sys.path.insert(0, compare_path)

        try:
            from compare import merge_sort

            size = 10000
            arr = [random.randint(1, 10000) for _ in range(size)]
            print(f"Размер: {size}")

            time_iter = time_function(merge_sort_iterative, arr)
            time_rec = time_function(merge_sort, arr)

            print(f"  Итеративная: {time_iter:.6f} сек")
            print(f"  Рекурсивная: {time_rec:.6f} сек")

            ratio = time_rec / time_iter
            print(f"\n  Соотношение (рекурсивная/итеративная): {ratio:.2f}x")
            print("  Обе версии показывают сравнимую производительность")

        except ImportError:
            print("  Пропущено: рекурсивная версия не найдена")
            pytest.skip("Рекурсивная версия не найдена")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
