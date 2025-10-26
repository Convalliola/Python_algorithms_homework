"""
Tests for two_sum function
"""
import pytest
from two_sum import two_sum


class TestTwoSum:
    """Test cases for two_sum function"""

    def test_basic_case(self):
        """Test with the example from the docstring"""
        arr = [-6, 0, 6, 7, 2, 15]
        k = 9
        result = two_sum(arr, k)
        # arr[3] = 7, arr[4] = 2, and 7 + 2 = 9
        assert result == (3, 4), f"Expected (3, 4), got {result}"
        assert arr[result[0]] + arr[result[1]] == k

    def test_positive_numbers(self):
        """Test with positive numbers only"""
        arr = [1, 2, 3, 4, 5]
        k = 9
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1], "Indices should be in ascending order"

    def test_negative_numbers(self):
        """Test with negative numbers"""
        arr = [-5, -3, -1, 0, 2, 4]
        k = -4
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]

    def test_with_zero(self):
        """Test when target sum involves zero"""
        arr = [0, 5, 3, 2]
        k = 5
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]

    def test_first_and_last_elements(self):
        """Test when the pair is first and last element"""
        arr = [1, 5, 3, 10]
        k = 11
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]

    def test_adjacent_elements(self):
        """Test when the pair consists of adjacent elements"""
        arr = [3, 7, 1, 9]
        k = 10
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]

    def test_duplicate_values(self):
        """Test with duplicate values in array"""
        arr = [3, 3, 6, 9]
        k = 6
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]

    def test_large_numbers(self):
        """Test with large numbers"""
        arr = [1000000, 500000, 250000, 125000]
        k = 1500000
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]

    def test_two_elements_only(self):
        """Test with minimum array size (2 elements)"""
        arr = [5, 7]
        k = 12
        result = two_sum(arr, k)
        assert result == (0, 1)
        assert arr[result[0]] + arr[result[1]] == k

    def test_negative_target(self):
        """Test when target sum is negative"""
        arr = [-10, -5, 0, 5, 10]
        k = -15
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]

    def test_zero_sum(self):
        """Test when target sum is zero"""
        arr = [-5, -2, 0, 2, 5]
        k = 0
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]

    def test_indices_order(self):
        """Verify that indices are always returned in ascending order"""
        arr = [10, 5, 3, 8, 2]
        k = 13
        result = two_sum(arr, k)
        assert result[0] < result[1], "First index should be less than second index"
        assert arr[result[0]] + arr[result[1]] == k
