"""
Тесты для функции permute из модуля permutations
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from permutations import permute


class TestPermute(unittest.TestCase):
    """Тесты для функции генерации перестановок"""

    def test_single_element(self):
        """Тест с одним элементом"""
        result = permute([1])
        expected = [[1]]
        self.assertEqual(result, expected)

    def test_two_elements(self):
        """Тест с двумя элементами"""
        result = permute([0, 1])
        expected = [[0, 1], [1, 0]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_three_elements(self):
        """Тест с тремя элементами"""
        result = permute([1, 2, 3])
        expected = [
            [1, 2, 3], [1, 3, 2],
            [2, 1, 3], [2, 3, 1],
            [3, 1, 2], [3, 2, 1]
        ]
        self.assertEqual(sorted(result), sorted(expected))

    def test_empty_list(self):
        """Тест с пустым списком"""
        result = permute([])
        expected = [[]]
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        """Тест с отрицательными числами"""
        result = permute([-1, 0, 1])
        # Проверяем количество перестановок (должно быть 3! = 6)
        self.assertEqual(len(result), 6)
        # Проверяем, что все элементы присутствуют в каждой перестановке
        for perm in result:
            self.assertEqual(sorted(perm), [-1, 0, 1])

    def test_duplicate_elements(self):
        """Тест с повторяющимися элементами (функция генерирует все перестановки, включая дубликаты)"""
        result = permute([1, 1, 2])
        # Для [1, 1, 2] будет 3! = 6 перестановок (с повторениями)
        self.assertEqual(len(result), 6)

    def test_four_elements(self):
        """Тест с четырьмя элементами"""
        result = permute([1, 2, 3, 4])
        # Проверяем количество перестановок (должно быть 4! = 24)
        self.assertEqual(len(result), 24)
        # Проверяем, что все перестановки уникальны
        self.assertEqual(len(result), len(set(tuple(p) for p in result)))

    def test_permutation_length(self):
        """Тест проверки длины каждой перестановки"""
        nums = [1, 2, 3, 4, 5]
        result = permute(nums)
        # Все перестановки должны иметь ту же длину, что и исходный массив
        for perm in result:
            self.assertEqual(len(perm), len(nums))

    def test_all_elements_present(self):
        """Тест проверки наличия всех элементов в каждой перестановке"""
        nums = [5, 10, 15, 20]
        result = permute(nums)
        for perm in result:
            self.assertEqual(sorted(perm), sorted(nums))

    def test_count_formula(self):
        """Тест проверки количества перестановок по формуле n!"""
        import math
        test_cases = [
            ([1], 1),
            ([1, 2], 2),
            ([1, 2, 3], 6),
            ([1, 2, 3, 4], 24),
            ([1, 2, 3, 4, 5], 120),
        ]
        for nums, expected_count in test_cases:
            with self.subTest(nums=nums):
                result = permute(nums)
                self.assertEqual(len(result), expected_count)
                self.assertEqual(len(result), math.factorial(len(nums)))

    def test_trace_parameter_false(self):
        """Тест с параметром trace=False (не должен выводить трассировку)"""
        # Этот тест просто проверяет, что функция работает с trace=False
        result = permute([1, 2], trace=False)
        self.assertEqual(len(result), 2)

    def test_trace_parameter_true(self):
        """Тест с параметром trace=True"""
        # Этот тест просто проверяет, что функция работает с trace=True
        # Вывод не проверяем, только корректность результата
        result = permute([1, 2], trace=True)
        self.assertEqual(len(result), 2)

    def test_strings(self):
        """Тест с символами (строками)"""
        result = permute(['a', 'b', 'c'])
        self.assertEqual(len(result), 6)
        # Проверяем, что каждая перестановка содержит все символы
        for perm in result:
            self.assertEqual(sorted(perm), ['a', 'b', 'c'])

    def test_mixed_types(self):
        """Тест со смешанными типами данных"""
        result = permute([1, 'a', 2.5])
        self.assertEqual(len(result), 6)
        # Проверяем, что все элементы присутствуют
        for perm in result:
            self.assertIn(1, perm)
            self.assertIn('a', perm)
            self.assertIn(2.5, perm)


class TestPermuteUniqueness(unittest.TestCase):
    """Тесты для проверки уникальности перестановок"""

    def test_all_unique(self):
        """Проверка, что все перестановки уникальны для массива без повторений"""
        nums = [1, 2, 3, 4]
        result = permute(nums)
        # Преобразуем списки в кортежи для проверки уникальности
        result_tuples = [tuple(p) for p in result]
        self.assertEqual(len(result_tuples), len(set(result_tuples)))


class TestPermuteEdgeCases(unittest.TestCase):
    """Тесты для граничных случаев"""

    def test_large_numbers(self):
        """Тест с большими числами"""
        result = permute([1000000, 2000000])
        self.assertEqual(len(result), 2)
        self.assertIn([1000000, 2000000], result)
        self.assertIn([2000000, 1000000], result)

    def test_zero_only(self):
        """Тест с массивом содержащим только нули"""
        result = permute([0])
        self.assertEqual(result, [[0]])

    def test_same_element_twice(self):
        """Тест с двумя одинаковыми элементами"""
        result = permute([5, 5])
        # Должно быть 2 перестановки: [5, 5] и [5, 5]
        self.assertEqual(len(result), 2)


if __name__ == '__main__':
    # Запуск тестов с подробным выводом
    unittest.main(verbosity=2)
