import pytest
from rabin_karp import rabin_karp


class TestRabinKarp:
    """Тесты для алгоритма Рабина-Карпа."""

    def test_single_occurrence(self):
        """Одно вхождение паттерна."""
        assert rabin_karp("hello world", "world") == [6]

    def test_multiple_occurrences(self):
        """Несколько вхождений паттерна."""
        assert rabin_karp("ABABDABACDABABCABAB", "ABAB") == [0, 10, 15]

    def test_overlapping_occurrences(self):
        """Перекрывающиеся вхождения."""
        assert rabin_karp("AAAA", "AA") == [0, 1, 2]
        assert rabin_karp("AABAACAADAABAABA", "AABA") == [0, 9, 12]

    def test_pattern_at_start(self):
        """Паттерн в начале строки."""
        assert rabin_karp("abcdef", "abc") == [0]

    def test_pattern_at_end(self):
        """Паттерн в конце строки."""
        assert rabin_karp("abcdef", "def") == [3]

    def test_pattern_equals_text(self):
        """Паттерн равен всему тексту."""
        assert rabin_karp("abc", "abc") == [0]

    def test_no_occurrence(self):
        """Паттерн не найден."""
        assert rabin_karp("hello world", "xyz") == []

    def test_empty_pattern(self):
        """Пустой паттерн."""
        assert rabin_karp("hello", "") == []

    def test_empty_text(self):
        """Пустой текст."""
        assert rabin_karp("", "abc") == []

    def test_both_empty(self):
        """Пустые текст и паттерн."""
        assert rabin_karp("", "") == []

    def test_pattern_longer_than_text(self):
        """Паттерн длиннее текста."""
        assert rabin_karp("ab", "abcd") == []

    def test_single_character_pattern(self):
        """Паттерн из одного символа."""
        assert rabin_karp("ababa", "a") == [0, 2, 4]
        assert rabin_karp("ababa", "b") == [1, 3]

    def test_single_character_text(self):
        """Текст из одного символа."""
        assert rabin_karp("a", "a") == [0]
        assert rabin_karp("a", "b") == []

    def test_case_sensitive(self):
        """Регистрозависимый поиск."""
        assert rabin_karp("Hello World", "hello") == []
        assert rabin_karp("Hello World", "Hello") == [0]

    def test_special_characters(self):
        """Специальные символы."""
        assert rabin_karp("a!b@c#d", "!b@") == [1]
        assert rabin_karp("hello\nworld", "\n") == [5]

    def test_unicode(self):
        """Unicode символы."""
        assert rabin_karp("привет мир", "мир") == [7]
        assert rabin_karp("абабаб", "аб") == [0, 2, 4]

    def test_repeated_pattern(self):
        """Повторяющийся паттерн."""
        assert rabin_karp("abcabcabc", "abc") == [0, 3, 6]

    def test_long_text(self):
        """Длинный текст."""
        text = "a" * 10000 + "b" + "a" * 10000
        assert rabin_karp(text, "b") == [10000]
        assert rabin_karp(text, "ab") == [9999]
        assert rabin_karp(text, "ba") == [10000]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
