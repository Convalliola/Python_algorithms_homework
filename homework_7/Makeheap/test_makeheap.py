import pytest
from makeheap import makeheap_n_log_n, makeheap, is_min_heap, sift_up, sift_down


class TestSiftOperations:
    """Тесты для функций sift_up и sift_down"""

    def test_sift_up_basic(self):
        heap = [1, 3, 5, 7, 9, 2]
        sift_up(heap, 5)
        assert is_min_heap(heap)
        assert heap[0] == 1

    def test_sift_up_to_root(self):
        heap = [5, 10, 15, 1]
        sift_up(heap, 3)
        assert heap[0] == 1
        assert is_min_heap(heap)

    def test_sift_down_basic(self):
        heap = [10, 2, 3, 4, 5]
        sift_down(heap, 0, len(heap))
        assert is_min_heap(heap)

    def test_sift_down_leaf(self):
        heap = [1, 2, 3, 4, 5]
        original = heap.copy()
        sift_down(heap, 4, len(heap))
        assert heap == original


class TestIsMinHeap:
    """ min-heap validation function"""

    def test_valid_min_heap(self):
        assert is_min_heap([1, 2, 3, 4, 5, 6, 7])
        assert is_min_heap([1, 3, 2, 7, 5, 8, 6])

    def test_invalid_min_heap(self):
        assert not is_min_heap([3, 1, 2, 4, 5])
        assert not is_min_heap([1, 2, 3, 0, 5])

    def test_empty_heap(self):
        assert is_min_heap([])

    def test_single_element(self):
        assert is_min_heap([42])

    def test_two_elements(self):
        assert is_min_heap([1, 2])
        assert not is_min_heap([2, 1])


class TestMakeheapNLogN:
    """тест метода O(N log N) """

    def test_empty_array(self):
        result = makeheap_n_log_n([])
        assert result == []
        assert is_min_heap(result)

    def test_single_element(self):
        result = makeheap_n_log_n([42])
        assert result == [42]
        assert is_min_heap(result)

    def test_two_elements(self):
        result = makeheap_n_log_n([5, 3])
        assert is_min_heap(result)
        assert result[0] == 3

    def test_simple_array(self):
        arr = [5, 3, 8, 1, 2, 7]
        result = makeheap_n_log_n(arr)
        assert is_min_heap(result)
        assert result[0] == 1
        assert sorted(result) == sorted(arr)

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = makeheap_n_log_n(arr)
        assert is_min_heap(result)
        assert result[0] == 1

    def test_reverse_sorted(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = makeheap_n_log_n(arr)
        assert is_min_heap(result)
        assert result[0] == 1

    def test_duplicates(self):
        arr = [5, 5, 5, 1, 1, 3, 3]
        result = makeheap_n_log_n(arr)
        assert is_min_heap(result)
        assert result[0] == 1
        assert sorted(result) == sorted(arr)

    def test_all_same_elements(self):
        arr = [7, 7, 7, 7, 7]
        result = makeheap_n_log_n(arr)
        assert is_min_heap(result)
        assert all(x == 7 for x in result)

    def test_negative_numbers(self):
        arr = [5, -3, 8, -1, 2, -7]
        result = makeheap_n_log_n(arr)
        assert is_min_heap(result)
        assert result[0] == -7
        assert sorted(result) == sorted(arr)

    def test_large_array(self):
        arr = list(range(100, 0, -1))
        result = makeheap_n_log_n(arr)
        assert is_min_heap(result)
        assert result[0] == 1

    def test_original_array_unchanged(self):
        arr = [5, 3, 8, 1, 2, 7]
        original = arr.copy()
        makeheap_n_log_n(arr)
        assert arr == original


class TestMakeheap:
    """тест метода O(N) """

    def test_empty_array(self):
        result = makeheap([])
        assert result == []
        assert is_min_heap(result)

    def test_single_element(self):
        result = makeheap([42])
        assert result == [42]
        assert is_min_heap(result)

    def test_two_elements(self):
        result = makeheap([5, 3])
        assert is_min_heap(result)
        assert result[0] == 3

    def test_simple_array(self):
        arr = [5, 3, 8, 1, 2, 7]
        result = makeheap(arr)
        assert is_min_heap(result)
        assert result[0] == 1
        assert sorted(result) == sorted(arr)

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = makeheap(arr)
        assert is_min_heap(result)
        assert result[0] == 1

    def test_reverse_sorted(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = makeheap(arr)
        assert is_min_heap(result)
        assert result[0] == 1

    def test_duplicates(self):
        arr = [5, 5, 5, 1, 1, 3, 3]
        result = makeheap(arr)
        assert is_min_heap(result)
        assert result[0] == 1
        assert sorted(result) == sorted(arr)

    def test_all_same_elements(self):
        arr = [7, 7, 7, 7, 7]
        result = makeheap(arr)
        assert is_min_heap(result)
        assert all(x == 7 for x in result)

    def test_negative_numbers(self):
        arr = [5, -3, 8, -1, 2, -7]
        result = makeheap(arr)
        assert is_min_heap(result)
        assert result[0] == -7
        assert sorted(result) == sorted(arr)

    def test_large_array(self):
        arr = list(range(100, 0, -1))
        result = makeheap(arr)
        assert is_min_heap(result)
        assert result[0] == 1

    def test_original_array_unchanged(self):
        arr = [5, 3, 8, 1, 2, 7]
        original = arr.copy()
        makeheap(arr)
        assert arr == original


class TestBothMethods:
    """тест на то, что оба метода создают валидную кучу с одинаковыми элементами"""

    @pytest.mark.parametrize("arr", [
        [5, 3, 8, 1, 2, 7],
        [1, 2, 3, 4, 5],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [5, 5, 5, 1, 1, 3, 3],
        [42],
        [],
        [-5, -10, 0, 15, -3],
        list(range(50)),
    ])
    def test_both_methods_produce_valid_heaps(self, arr):
        heap1 = makeheap_n_log_n(arr)
        heap2 = makeheap(arr)

        assert is_min_heap(heap1)
        assert is_min_heap(heap2)
        assert sorted(heap1) == sorted(arr)
        assert sorted(heap2) == sorted(arr)

        if arr:
            assert heap1[0] == min(arr)
            assert heap2[0] == min(arr)


class TestEdgeCases:
    """Корнер кейсы"""

    def test_very_large_numbers(self):
        arr = [10**9, 10**8, 10**7, 1, 2, 3]
        heap1 = makeheap_n_log_n(arr)
        heap2 = makeheap(arr)

        assert is_min_heap(heap1)
        assert is_min_heap(heap2)
        assert heap1[0] == 1
        assert heap2[0] == 1

    def test_mixed_positive_negative(self):
        arr = [-100, 50, -50, 100, 0, -25, 25]
        heap1 = makeheap_n_log_n(arr)
        heap2 = makeheap(arr)

        assert is_min_heap(heap1)
        assert is_min_heap(heap2)
        assert heap1[0] == -100
        assert heap2[0] == -100

    def test_three_elements(self):
        arr = [3, 1, 2]
        heap1 = makeheap_n_log_n(arr)
        heap2 = makeheap(arr)

        assert is_min_heap(heap1)
        assert is_min_heap(heap2)
        assert heap1[0] == 1
        assert heap2[0] == 1

    def test_power_of_two_size(self):
        # Perfect binary tree
        arr = list(range(16, 0, -1))
        heap1 = makeheap_n_log_n(arr)
        heap2 = makeheap(arr)

        assert is_min_heap(heap1)
        assert is_min_heap(heap2)
        assert len(heap1) == 16
        assert len(heap2) == 16

    def test_almost_power_of_two_size(self):
        arr = list(range(15, 0, -1))
        heap1 = makeheap_n_log_n(arr)
        heap2 = makeheap(arr)

        assert is_min_heap(heap1)
        assert is_min_heap(heap2)
        assert len(heap1) == 15
        assert len(heap2) == 15


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
