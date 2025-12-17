import pytest
from lcs import lcs, lcs_length


class TestLCS:
    """Тесты для алгоритма LCS"""

    def test_example_from_task(self):
        """Пример из условия задачи"""
        assert lcs("AGGTAB", "GXTXAYB") == "GTAB"

    def test_basic_cases(self):
        """Базовые случаи"""
        assert lcs("ABCDGH", "AEDFHR") == "ADH"
        assert lcs("ABC", "AC") == "AC"
        assert lcs("ABCBDAB", "BDCABA") == "BDAB"

    def test_identical_strings(self):
        """Одинаковые строки"""
        assert lcs("ABC", "ABC") == "ABC"
        assert lcs("HELLO", "HELLO") == "HELLO"

    def test_one_string_is_subsequence(self):
        """Одна строка — подпоследовательность другой"""
        assert lcs("AC", "ABC") == "AC"
        assert lcs("ABC", "AABBCC") == "ABC"

    def test_no_common_subsequence(self):
        """Нет общих символов """
        assert lcs("ABC", "XYZ") == ""
        assert lcs("AAA", "BBB") == ""

    def test_empty_strings(self):
        """Пустые строки """
        assert lcs("", "") == ""
        assert lcs("ABC", "") == ""
        assert lcs("", "ABC") == ""

    def test_single_character(self):
        """Строки из одного символа"""
        assert lcs("A", "A") == "A"
        assert lcs("A", "B") == ""
        assert lcs("A", "BAB") == "A"

    def test_repeated_characters(self):
        """Повторяющиеся символы."""
        assert lcs("AAAA", "AA") == "AA"
        # LCS может быть "AAB" или "ABB", обе длины 3
        assert len(lcs("AABB", "ABAB")) == 3

    def test_reverse_strings(self):
        """Обратные строки"""
        result = lcs("ABCD", "DCBA")
        assert len(result) == 1  # любой один символ

    def test_long_strings(self):
        """Длинные строки"""
        s1 = "A" * 100 + "B" * 100
        s2 = "A" * 50 + "C" * 50 + "B" * 50
        result = lcs(s1, s2)
        assert len(result) == 100  # 50 A + 50 B

    def test_case_sensitive(self):
        """Регистрозависимость"""
        assert lcs("abc", "ABC") == ""
        # "AbC" и "aBc" не имеют общих символов (b != B)
        assert lcs("AbC", "aBc") == ""
        assert lcs("AbC", "abc") == "b"

    def test_special_characters(self):
        """Специальные символы"""
        assert lcs("a!b@c", "!@#") == "!@"
        assert lcs("hello\nworld", "h\nw") == "h\nw"

    def test_unicode(self):
        """Unicode символы."""
        assert lcs("привет", "привет") == "привет"
        assert lcs("абв", "бвг") == "бв"

    def test_symmetry(self):
        """Симметричность: длина LCS не зависит от порядка аргументов"""
        s1, s2 = "AGGTAB", "GXTXAYB"
        assert len(lcs(s1, s2)) == len(lcs(s2, s1))


class TestLCSLength:
    """Тесты для функции lcs_length."""

    def test_example_from_task(self):
        """Пример из условия задачи."""
        assert lcs_length("AGGTAB", "GXTXAYB") == 4

    def test_consistency_with_lcs(self):
        """Длина совпадает с len(lcs())"""
        pairs = [
            ("ABCDGH", "AEDFHR"),
            ("ABC", "AC"),
            ("ABCBDAB", "BDCABA"),
            ("ABC", "XYZ"),
            ("", "ABC"),
        ]
        for s1, s2 in pairs:
            assert lcs_length(s1, s2) == len(lcs(s1, s2))

    def test_empty_strings(self):
        """Пустые строки"""
        assert lcs_length("", "") == 0
        assert lcs_length("ABC", "") == 0

    def test_identical_strings(self):
        """Одинаковые строки"""
        assert lcs_length("HELLO", "HELLO") == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
