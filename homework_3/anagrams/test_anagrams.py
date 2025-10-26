"""
Тесты для модуля anagrams
"""
import pytest
from anagrams import anagrams_, word_to_table



class TestAnagrams:
    """Тесты для функции anagrams_"""

    def test_basic_anagrams(self):
        words = ['кот', 'ток', 'кит', 'тик']
        result = list(anagrams_(words))
        assert len(result) == 2
        groups = [sorted(group) for group in result]
        assert sorted(['кот', 'ток']) in groups
        assert sorted(['кит', 'тик']) in groups

    def test_no_anagrams(self):
        #слова без анаграмм"""
        words = ['кот', 'пес', 'дом']
        result = list(anagrams_(words))
        assert len(result) == 3
        for group in result:
            assert len(group) == 1

    def test_all_anagrams(self):
        words = ['кот', 'ток', 'кто']
        result = list(anagrams_(words))
        assert len(result) == 1
        assert sorted(result[0]) == sorted(words)

    def test_empty_list(self):
        #пустой список
        result = list(anagrams_([]))
        assert result == []

    def test_single_word(self):
        # один элемент
        result = list(anagrams_(['кот']))
        assert len(result) == 1
        assert result[0] == ['кот']

    def test_multiple_groups(self):
        # несколько групп анаграмм
        words = ['кот', 'ток', 'пес', 'сеп', 'дом']
        result = list(anagrams_(words))
        assert len(result) == 3

        # Проверяем размеры групп
        group_sizes = sorted([len(group) for group in result])
        assert group_sizes == [1, 2, 2]

    def test_different_length_words(self):
        words = ['кот', 'коты', 'ток']
        result = list(anagrams_(words))
        assert len(result) == 2

        groups = [sorted(group) for group in result]
        assert sorted(['кот', 'ток']) in groups
        assert ['коты'] in groups

    def test_repeated_words(self):
        """Повторяющиеся слова"""
        words = ['кот', 'кот', 'ток']
        result = list(anagrams_(words))
        assert len(result) == 1
        assert sorted(result[0]) == ['кот', 'кот', 'ток']

    def test_with_yo(self):
        # 'ёж' и 'жё' - анаграммы, 'еж' - отдельно
        words = ['ёж', 'жё', 'еж']
        result = list(anagrams_(words))
        assert len(result) == 2

    def test_long_words(self):
        words = ['автомобиль', 'мобильавто', 'велосипед']
        result = list(anagrams_(words))
        assert len(result) == 2

        groups = [sorted(group) for group in result]
        # Проверяем, что анаграммы сгруппированы
        anagram_group = [g for g in groups if len(g) == 2][0]
        assert 'автомобиль' in anagram_group
        assert 'мобильавто' in anagram_group
