import pytest
from kmp import kmp_search, compute_prefix_function


class TestKMPSearch:
    """Тесты для алгоритма КМП."""

    def test_single_occurrence(self):
        """Одно вхождение паттерна"""
        assert kmp_search("hello world", "world") == [6]

    def test_multiple_occurrences(self):
        """Несколько вхождений паттерна"""
        assert kmp_search("ABABDABACDABABCABAB", "ABAB") == [0, 10, 15]

    def test_overlapping_occurrences(self):
        """Перекрывающиеся вхождения"""
        assert kmp_search("AAAA", "AA") == [0, 1, 2]
        assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]

    def test_pattern_at_start(self):
        """Паттерн в начале строки"""
        assert kmp_search("abcdef", "abc") == [0]

    def test_pattern_at_end(self):
        """Паттерн в конце строки """
        assert kmp_search("abcdef", "def") == [3]

    def test_pattern_equals_text(self):
        """Паттерн равен всему тексту """
        assert kmp_search("abc", "abc") == [0]

    def test_no_occurrence(self):
        """Паттерн не найден."""
        assert kmp_search("hello world", "xyz") == []

    def test_empty_pattern(self):
        """Пустой паттерн """
        assert kmp_search("hello", "") == []

    def test_empty_text(self):
        """Пустой текст """
        assert kmp_search("", "abc") == []

    def test_both_empty(self):
        """Пустые текст и паттерн """
        assert kmp_search("", "") == []

    def test_pattern_longer_than_text(self):
        """Паттерн длиннее текста."""
        assert kmp_search("ab", "abcd") == []

    def test_single_character_pattern(self):
        """Паттерн из одного символа """
        assert kmp_search("ababa", "a") == [0, 2, 4]
        assert kmp_search("ababa", "b") == [1, 3]

    def test_single_character_text(self):
        """Текст из одного символа """
        assert kmp_search("a", "a") == [0]
        assert kmp_search("a", "b") == []

    def test_case_sensitive(self):
        """Регистрозависимый поиск."""
        assert kmp_search("Hello World", "hello") == []
        assert kmp_search("Hello World", "Hello") == [0]

    def test_special_characters(self):
        """Специальные символы """
        assert kmp_search("a!b@c#d", "!b@") == [1]
        assert kmp_search("hello\nworld", "\n") == [5]

    def test_unicode(self):
        """Unicode символы """
        assert kmp_search("привет мир", "мир") == [7]
        assert kmp_search("абабаб", "аб") == [0, 2, 4]

    def test_repeated_pattern(self):
        """Повторяющийся паттерн"""
        assert kmp_search("abcabcabc", "abc") == [0, 3, 6]

    def test_long_text(self):
        """Длинный текст"""
        text = "a" * 10000 + "b" + "a" * 10000
        assert kmp_search(text, "b") == [10000]
        assert kmp_search(text, "ab") == [9999]
        assert kmp_search(text, "ba") == [10000]


class TestPrefixFunction:
    """Тесты для префикс-функции."""

    def test_no_repeats(self):
        """Строка без повторов."""
        assert compute_prefix_function("ABCD") == [0, 0, 0, 0]

    def test_simple_repeat(self):
        """Простой повтор."""
        assert compute_prefix_function("ABAB") == [0, 0, 1, 2]

    def test_all_same(self):
        """Все символы одинаковые."""
        assert compute_prefix_function("AAAA") == [0, 1, 2, 3]

    def test_complex_pattern(self):
        """Сложный паттерн."""
        assert compute_prefix_function("AAACAAAA") == [0, 1, 2, 0, 1, 2, 3, 3]
        assert compute_prefix_function("AABA") == [0, 1, 0, 1]

    def test_single_character(self):
        """Один символ."""
        assert compute_prefix_function("A") == [0]

    def test_two_characters(self):
        """Два символа."""
        assert compute_prefix_function("AA") == [0, 1]
        assert compute_prefix_function("AB") == [0, 0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
