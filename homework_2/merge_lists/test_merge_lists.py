"""
Тесты для задачи слияния двух отсортированных односвязных списков
"""
import pytest
from merge_lists import (
    merge_two_lists_with_dummy,
    merge_two_lists_without_dummy,
    create_linked_list,
    linked_list_to_array
)


class TestMergeTwoSortedLists:
    """Тесты для обеих реализаций слияния списков"""

    # Параметризуем тесты для проверки обоих способов
    @pytest.fixture(params=[
        merge_two_lists_with_dummy,
        merge_two_lists_without_dummy
    ])
    def merge_function(self, request):
        """Фикстура для тестирования обеих реализаций"""
        return request.param

    def test_example_case(self, merge_function):
        """Тест примера из условия задачи"""
        list1 = create_linked_list([1, 2, 4])
        list2 = create_linked_list([1, 3, 4])
        result = merge_function(list1, list2)
        assert linked_list_to_array(result) == [1, 1, 2, 3, 4, 4]

    def test_empty_lists(self, merge_function):
        """Тест со случаем, когда оба списка пусты"""
        list1 = create_linked_list([])
        list2 = create_linked_list([])
        result = merge_function(list1, list2)
        assert linked_list_to_array(result) == []

    def test_first_list_empty(self, merge_function):
        """Тест когда первый список пуст"""
        list1 = create_linked_list([])
        list2 = create_linked_list([0])
        result = merge_function(list1, list2)
        assert linked_list_to_array(result) == [0]

    def test_second_list_empty(self, merge_function):
        """Тест когда второй список пуст"""
        list1 = create_linked_list([1])
        list2 = create_linked_list([])
        result = merge_function(list1, list2)
        assert linked_list_to_array(result) == [1]

    def test_different_lengths(self, merge_function):
        """Тест со списками разной длины"""
        list1 = create_linked_list([1, 3, 5, 7, 9])
        list2 = create_linked_list([2, 4])
        result = merge_function(list1, list2)
        assert linked_list_to_array(result) == [1, 2, 3, 4, 5, 7, 9]

    def test_no_overlapping_values(self, merge_function):
        """Тест когда все элементы одного списка меньше другого"""
        list1 = create_linked_list([1, 2, 3])
        list2 = create_linked_list([4, 5, 6])
        result = merge_function(list1, list2)
        assert linked_list_to_array(result) == [1, 2, 3, 4, 5, 6]

    def test_identical_values(self, merge_function):
        """Тест со списками с одинаковыми значениями"""
        list1 = create_linked_list([1, 1, 1])
        list2 = create_linked_list([1, 1, 1])
        result = merge_function(list1, list2)
        assert linked_list_to_array(result) == [1, 1, 1, 1, 1, 1]

    def test_single_element_lists(self, merge_function):
        """Тест с односложными списками"""
        list1 = create_linked_list([5])
        list2 = create_linked_list([3])
        result = merge_function(list1, list2)
        assert linked_list_to_array(result) == [3, 5]

    def test_negative_numbers(self, merge_function):
        """Тест с отрицательными числами"""
        list1 = create_linked_list([-3, -1, 2])
        list2 = create_linked_list([-2, 0, 4])
        result = merge_function(list1, list2)
        assert linked_list_to_array(result) == [-3, -2, -1, 0, 2, 4]

    def test_large_lists(self, merge_function):
        """Тест с большими списками"""
        list1 = create_linked_list(list(range(0, 100, 2)))  # четные от 0 до 98
        list2 = create_linked_list(list(range(1, 100, 2)))  # нечетные от 1 до 99
        result = merge_function(list1, list2)
        assert linked_list_to_array(result) == list(range(100))


class TestHelperFunctions:
    """Тесты для вспомогательных функций"""

    def test_create_linked_list_empty(self):
        """Тест создания пустого списка"""
        result = create_linked_list([])
        assert result is None

    def test_create_linked_list_single(self):
        """Тест создания списка из одного элемента"""
        result = create_linked_list([42])
        assert result.val == 42
        assert result.next is None

    def test_create_linked_list_multiple(self):
        """Тест создания списка из нескольких элементов"""
        result = create_linked_list([1, 2, 3])
        assert result.val == 1
        assert result.next.val == 2
        assert result.next.next.val == 3
        assert result.next.next.next is None

    def test_linked_list_to_array_empty(self):
        """Тест преобразования пустого списка"""
        result = linked_list_to_array(None)
        assert result == []

    def test_linked_list_to_array_single(self):
        """Тест преобразования списка из одного элемента"""
        head = create_linked_list([42])
        result = linked_list_to_array(head)
        assert result == [42]

    def test_linked_list_to_array_multiple(self):
        """Тест преобразования списка из нескольких элементов"""
        head = create_linked_list([1, 2, 3, 4, 5])
        result = linked_list_to_array(head)
        assert result == [1, 2, 3, 4, 5]
