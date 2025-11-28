import pytest
from k_th_minheap import (
    MinHeap,
    find_kth_largest_custom,
    find_kth_largest_heapq,
    find_kth_largest_heapq_simple
)


class TestMinHeap:
    """тест кастомной MinHeap"""

    def test_empty_heap(self):
        heap = MinHeap()
        assert heap.size() == 0
        assert heap.peek() is None
        assert heap.pop() is None

    def test_single_element(self):
        heap = MinHeap()
        heap.push(5)
        assert heap.size() == 1
        assert heap.peek() == 5
        assert heap.pop() == 5
        assert heap.size() == 0

    def test_multiple_elements(self):
        heap = MinHeap()
        elements = [5, 3, 8, 1, 2, 7]
        for elem in elements:
            heap.push(elem)

        result = []
        while heap.size() > 0:
            result.append(heap.pop())

        assert result == sorted(elements)

    def test_heap_property_maintained(self):
        heap = MinHeap()
        elements = [10, 5, 15, 3, 7, 12, 20]
        for elem in elements:
            heap.push(elem)

        for i in range(len(heap.heap)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap.heap):
                assert heap.heap[i] <= heap.heap[left]
            if right < len(heap.heap):
                assert heap.heap[i] <= heap.heap[right]

    def test_peek_does_not_remove(self):
        heap = MinHeap()
        heap.push(5)
        heap.push(3)
        heap.push(8)

        assert heap.peek() == 3
        assert heap.size() == 3
        assert heap.peek() == 3  # Still 3


class TestKthLargestCustom:
    """тест функции find_kth_largest_custom"""

    def test_basic_example(self):
        assert find_kth_largest_custom([3, 2, 1, 5, 6, 4], 2) == 5

    def test_single_element(self):
        assert find_kth_largest_custom([1], 1) == 1

    def test_two_elements(self):
        assert find_kth_largest_custom([1, 2], 1) == 2
        assert find_kth_largest_custom([1, 2], 2) == 1

    def test_k_equals_1(self):
        assert find_kth_largest_custom([1, 2, 3, 4, 5], 1) == 5

    def test_k_equals_n(self):
        assert find_kth_largest_custom([1, 2, 3, 4, 5], 5) == 1

    def test_duplicates(self):
        assert find_kth_largest_custom([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    def test_all_same(self):
        assert find_kth_largest_custom([5, 5, 5, 5, 5], 3) == 5

    def test_sorted_ascending(self):
        assert find_kth_largest_custom([1, 2, 3, 4, 5, 6, 7], 3) == 5

    def test_sorted_descending(self):
        assert find_kth_largest_custom([7, 6, 5, 4, 3, 2, 1], 3) == 5

    def test_negative_numbers(self):
        assert find_kth_largest_custom([-1, -2, -3, -4, -5], 2) == -2

    def test_mixed_positive_negative(self):
        assert find_kth_largest_custom([-5, 0, 5, -3, 3], 2) == 3

    def test_large_k(self):
        nums = list(range(100))
        # 90th largest in [0..99] = 10 (99, 98, 97, ..., 11, 10)
        assert find_kth_largest_custom(nums, 90) == 10

    def test_invalid_k_zero(self):
        with pytest.raises(ValueError):
            find_kth_largest_custom([1, 2, 3], 0)

    def test_invalid_k_negative(self):
        with pytest.raises(ValueError):
            find_kth_largest_custom([1, 2, 3], -1)

    def test_invalid_k_too_large(self):
        with pytest.raises(ValueError):
            find_kth_largest_custom([1, 2, 3], 4)

    def test_empty_array(self):
        with pytest.raises(ValueError):
            find_kth_largest_custom([], 1)


class TestKthLargestHeapq:
    """тест функции find_kth_largest_heapq"""

    def test_basic_example(self):
        assert find_kth_largest_heapq([3, 2, 1, 5, 6, 4], 2) == 5

    def test_single_element(self):
        assert find_kth_largest_heapq([1], 1) == 1

    def test_duplicates(self):
        assert find_kth_largest_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    def test_all_same(self):
        assert find_kth_largest_heapq([5, 5, 5, 5, 5], 3) == 5

    def test_negative_numbers(self):
        assert find_kth_largest_heapq([-1, -2, -3, -4, -5], 2) == -2

    def test_invalid_input(self):
        with pytest.raises(ValueError):
            find_kth_largest_heapq([1, 2, 3], 0)


class TestKthLargestSimple:
    """Test find_kth_largest_heapq_simple function"""

    def test_basic_example(self):
        assert find_kth_largest_heapq_simple([3, 2, 1, 5, 6, 4], 2) == 5

    def test_single_element(self):
        assert find_kth_largest_heapq_simple([1], 1) == 1

    def test_duplicates(self):
        assert find_kth_largest_heapq_simple([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


class TestAllImplementationsConsistent:
    """тест на то, что все три метода дают одинаковые результаты"""

    @pytest.mark.parametrize("nums,k", [
        ([3, 2, 1, 5, 6, 4], 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
        ([1], 1),
        ([1, 2], 2),
        ([7, 6, 5, 4, 3, 2, 1], 3),
        ([1, 2, 3, 4, 5, 6, 7], 1),
        ([5, 5, 5, 5, 5], 3),
        ([-5, -10, 0, 15, -3], 2),
        (list(range(100)), 50),
        (list(range(100, 0, -1)), 25),
    ])
    def test_all_methods_agree(self, nums, k):
        result_custom = find_kth_largest_custom(nums, k)
        result_heapq = find_kth_largest_heapq(nums, k)
        result_simple = find_kth_largest_heapq_simple(nums, k)

        assert result_custom == result_heapq == result_simple

    @pytest.mark.parametrize("nums,k", [
        ([3, 2, 1, 5, 6, 4], 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
        ([7, 6, 5, 4, 3, 2, 1], 3),
    ])
    def test_matches_sorted(self, nums, k):
        result_custom = find_kth_largest_custom(nums, k)
        sorted_desc = sorted(nums, reverse=True)
        expected = sorted_desc[k - 1]

        assert result_custom == expected


class TestEdgeCases:
    """корнер кейсы"""

    def test_very_large_numbers(self):
        nums = [10**9, 10**8, 10**7, 1, 2, 3]
        assert find_kth_largest_custom(nums, 2) == 10**8

    def test_k_equals_middle(self):
        nums = list(range(1, 100))
        k = 50
        result = find_kth_largest_custom(nums, k)
        assert result == sorted(nums, reverse=True)[k - 1]

    def test_power_of_two_size(self):
        nums = list(range(1, 17))  # 16 элементов
        assert find_kth_largest_custom(nums, 8) == 9

    def test_odd_size(self):
        nums = list(range(1, 16))  # 15 элементов
        assert find_kth_largest_custom(nums, 8) == 8

    def test_duplicates_at_k_position(self):
        nums = [1, 2, 2, 2, 3, 4, 5]
        # 2nd largest should be 4
        assert find_kth_largest_custom(nums, 2) == 4

    def test_many_duplicates(self):
        nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        assert find_kth_largest_custom(nums, 4) == 2


class TestPerformance:
    """производительность"""

    def test_large_n_small_k(self):
        """эффективен когда k << N"""
        nums = list(range(10000))
        result = find_kth_largest_custom(nums, 10)
        assert result == 9990

    def test_large_n_large_k(self):
        nums = list(range(1000))
        result = find_kth_largest_custom(nums, 990)
        # 990ый самый большой в [0..999] = 10 (999, 998, ..., 11, 10)
        assert result == 10


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
