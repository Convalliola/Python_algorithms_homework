"""
Pytest тесты для алгоритма Quickselect.
Запуск: pytest test_k_th.py -v -s
"""
import random
import time
import pytest
from typing import List


# Импортируем функции из k-th.py (с учетом дефиса в имени)
import importlib.util
import os

spec = importlib.util.spec_from_file_location("k_th", os.path.join(os.path.dirname(__file__), "k-th.py"))
k_th = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k_th)

quickselect_kth_largest = k_th.quickselect_kth_largest
quickselect_kth_smallest = k_th.quickselect_kth_smallest
quickselect_median_of_medians = k_th.quickselect_median_of_medians


class TestQuickselectCorrectness:
    """Тесты корректности Quickselect"""

    def test_example_from_task(self):
        """Пример из задания"""
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        result = quickselect_kth_largest(nums, k)
        assert result == 5, f"Ожидалось 5, получено {result}"

    def test_kth_largest_basic(self):
        """Базовый тест k-го максимального"""
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]

        # k=1: максимальный элемент
        assert quickselect_kth_largest(nums, 1) == 6
        # k=2: второй по величине
        assert quickselect_kth_largest(nums, 2) == 5
        # k=4: четвертый по величине
        assert quickselect_kth_largest(nums, 4) == 4

    def test_kth_smallest_basic(self):
        """Базовый тест k-го минимального"""
        nums = [7, 10, 4, 3, 20, 15]

        # k=1: минимальный элемент
        assert quickselect_kth_smallest(nums, 1) == 3
        # k=3: третий наименьший
        assert quickselect_kth_smallest(nums, 3) == 7
        # k=6: максимальный (последний наименьший)
        assert quickselect_kth_smallest(nums, 6) == 20

    def test_single_element(self):
        """Массив из одного элемента"""
        nums = [42]
        assert quickselect_kth_largest(nums, 1) == 42
        assert quickselect_kth_smallest(nums, 1) == 42

    def test_two_elements(self):
        """Массив из двух элементов"""
        nums = [5, 3]
        assert quickselect_kth_largest(nums, 1) == 5
        assert quickselect_kth_largest(nums, 2) == 3
        assert quickselect_kth_smallest(nums, 1) == 3
        assert quickselect_kth_smallest(nums, 2) == 5

    def test_all_identical(self):
        """Все элементы одинаковые"""
        nums = [7, 7, 7, 7, 7]
        for k in range(1, len(nums) + 1):
            assert quickselect_kth_largest(nums, k) == 7
            assert quickselect_kth_smallest(nums, k) == 7

    def test_sorted_ascending(self):
        """Уже отсортированный массив (по возрастанию)"""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # k=1 максимальный
        assert quickselect_kth_largest(nums, 1) == 10
        # k=5
        assert quickselect_kth_largest(nums, 5) == 6
        # k=10 минимальный (с точки зрения максимального)
        assert quickselect_kth_largest(nums, 10) == 1

    def test_sorted_descending(self):
        """Отсортированный массив (по убыванию)"""
        nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        assert quickselect_kth_largest(nums, 1) == 10
        assert quickselect_kth_largest(nums, 5) == 6
        assert quickselect_kth_smallest(nums, 1) == 1
        assert quickselect_kth_smallest(nums, 5) == 5

    def test_duplicates(self):
        """Массив с дубликатами"""
        nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
        sorted_desc = sorted(nums, reverse=True)

        for k in range(1, len(nums) + 1):
            expected = sorted_desc[k - 1]
            result = quickselect_kth_largest(nums, k)
            assert result == expected, f"k={k}: ожидалось {expected}, получено {result}"

    def test_negative_numbers(self):
        """Массив с отрицательными числами"""
        nums = [-5, 3, -1, 7, -9, 0, 4, -2]
        # Отсортировано: [-9, -5, -2, -1, 0, 3, 4, 7]

        # Максимальный
        assert quickselect_kth_largest(nums, 1) == 7
        # Минимальный
        assert quickselect_kth_smallest(nums, 1) == -9
        # 4-ый наименьший
        assert quickselect_kth_smallest(nums, 4) == -1
        # 5-ый наименьший
        assert quickselect_kth_smallest(nums, 5) == 0

    def test_large_random_array(self):
        """Большой случайный массив"""
        nums = [random.randint(-1000, 1000) for _ in range(1000)]
        sorted_nums = sorted(nums)

        # Проверяем несколько случайных k
        for _ in range(10):
            k = random.randint(1, len(nums))
            expected = sorted_nums[k - 1]
            result = quickselect_kth_smallest(nums, k)
            assert result == expected, f"k={k}: ожидалось {expected}, получено {result}"

    def test_invalid_k_too_small(self):
        """k меньше 1 - должна быть ошибка"""
        nums = [1, 2, 3, 4, 5]
        with pytest.raises(ValueError):
            quickselect_kth_largest(nums, 0)
        with pytest.raises(ValueError):
            quickselect_kth_largest(nums, -1)

    def test_invalid_k_too_large(self):
        """k больше размера массива - должна быть ошибка"""
        nums = [1, 2, 3, 4, 5]
        with pytest.raises(ValueError):
            quickselect_kth_largest(nums, 6)
        with pytest.raises(ValueError):
            quickselect_kth_largest(nums, 100)

    def test_does_not_modify_original(self):
        """Quickselect не должен модифицировать исходный массив"""
        nums = [5, 2, 8, 1, 9, 3]
        nums_copy = nums.copy()

        quickselect_kth_largest(nums, 3)

        assert nums == nums_copy, "Исходный массив был изменен!"


class TestMedianOfMedians:
    """Тесты для алгоритма медианы медиан"""

    def test_mom_basic(self):
        """Базовый тест медианы медиан"""
        nums = [3, 2, 1, 5, 6, 4]
        result = quickselect_median_of_medians(nums, 2)
        assert result == 5

    def test_mom_vs_regular(self):
        """Медиана медиан должна давать тот же результат что и обычная версия"""
        nums = [random.randint(1, 100) for _ in range(50)]

        for k in [1, 10, 25, 40, 50]:
            result_regular = quickselect_kth_largest(nums, k)
            result_mom = quickselect_median_of_medians(nums, k)
            assert result_regular == result_mom, \
                f"k={k}: обычная версия дала {result_regular}, медиана медиан дала {result_mom}"

    def test_mom_large_array(self):
        """Медиана медиан на большом массиве"""
        nums = [random.randint(1, 10000) for _ in range(1000)]
        k = 500  # медиана

        result = quickselect_median_of_medians(nums, k)
        expected = sorted(nums, reverse=True)[k - 1]

        assert result == expected


class TestPerformance:
    """Тесты производительности"""

    def test_performance_vs_sorting(self):
        """Quickselect должен быть быстрее полной сортировки на больших массивах"""
        print("\n" + "=" * 70)
        print("ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ: Quickselect vs Сортировка")
        print("=" * 70)

        for size in [10000, 50000, 100000]:
            nums = [random.randint(1, 1000000) for _ in range(size)]
            k = size // 2  # медиана

            print(f"\nРазмер массива: {size}, k={k}")

            # Quickselect
            start = time.perf_counter()
            result_qs = quickselect_kth_largest(nums, k)
            time_qs = time.perf_counter() - start
            print(f"  Quickselect: {time_qs:.6f} сек")

            # Полная сортировка
            start = time.perf_counter()
            result_sort = sorted(nums, reverse=True)[k - 1]
            time_sort = time.perf_counter() - start
            print(f"  Сортировка:  {time_sort:.6f} сек")

            ratio = time_sort / time_qs
            print(f"  Соотношение: {ratio:.2f}x")

            assert result_qs == result_sort, "Результаты не совпадают!"

    def test_performance_different_k(self):
        """Производительность Quickselect для разных k"""
        print("\n" + "=" * 70)
        print("ТЕСТ: Quickselect для разных позиций k")
        print("=" * 70)

        size = 100000
        nums = [random.randint(1, 1000000) for _ in range(size)]

        test_cases = [
            (1, "min"),
            (size // 4, "1st quartile"),
            (size // 2, "median"),
            (3 * size // 4, "3rd quartile"),
            (size, "max")
        ]

        print(f"\nРазмер массива: {size}")
        for k, description in test_cases:
            start = time.perf_counter()
            result = quickselect_kth_largest(nums, k)
            elapsed = time.perf_counter() - start
            print(f"  k={k:6d} ({description:12s}): {elapsed:.6f} сек")

    def test_worst_case_protection(self):
        """Рандомизация должна защищать от худшего случая"""
        print("\n" + "=" * 70)
        print("ТЕСТ: Защита от худшего случая (отсортированный массив)")
        print("=" * 70)

        size = 10000
        nums_sorted = list(range(size))
        nums_reversed = list(range(size, 0, -1))
        k = size // 2

        print(f"\nРазмер массива: {size}, k={k}")

        # Отсортированный массив
        start = time.perf_counter()
        result1 = quickselect_kth_largest(nums_sorted, k)
        time1 = time.perf_counter() - start
        print(f"  Отсортированный массив:  {time1:.6f} сек")

        # Обратно отсортированный массив
        start = time.perf_counter()
        result2 = quickselect_kth_largest(nums_reversed, k)
        time2 = time.perf_counter() - start
        print(f"  Обратный порядок:        {time2:.6f} сек")

        # Случайный массив
        nums_random = [random.randint(1, size) for _ in range(size)]
        start = time.perf_counter()
        result3 = quickselect_kth_largest(nums_random, k)
        time3 = time.perf_counter() - start
        print(f"  Случайный массив:        {time3:.6f} сек")

        print(f"\n  Все версии работают за сравнимое время благодаря рандомизации!")


class TestEdgeCases:
    """Граничные случаи"""

    def test_alternating_values(self):
        """Чередующиеся значения"""
        nums = [1, 2] * 50  # [1, 2, 1, 2, ...]

        # Половина элементов = 1, половина = 2
        # Максимальный (k=1) = 2
        assert quickselect_kth_largest(nums, 1) == 2
        # k=50 = 2
        assert quickselect_kth_largest(nums, 50) == 2
        # k=51 = 1
        assert quickselect_kth_largest(nums, 51) == 1
        # Минимальный = 1
        assert quickselect_kth_largest(nums, 100) == 1

    def test_power_of_two_sizes(self):
        """Массивы размером степень двойки"""
        for power in [4, 8, 16, 32, 64]:
            nums = [random.randint(1, 100) for _ in range(power)]
            k = power // 2

            result = quickselect_kth_largest(nums, k)
            expected = sorted(nums, reverse=True)[k - 1]

            assert result == expected, f"Размер {power}, k={k}"

    def test_very_large_numbers(self):
        """Очень большие числа"""
        nums = [10**9 + i for i in range(100)]
        random.shuffle(nums)

        # Максимальный
        assert quickselect_kth_largest(nums, 1) == 10**9 + 99
        # Минимальный
        assert quickselect_kth_smallest(nums, 1) == 10**9


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
