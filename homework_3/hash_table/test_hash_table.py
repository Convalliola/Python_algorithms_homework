"""
Тесты для хеш-таблицы
"""
import pytest
from hash_table import HashTable


class TestHashTableBasics:
    """Базовые тесты функциональности хеш-таблицы"""

    def test_insert_and_search(self):
        """Тест вставки и поиска элемента"""
        ht = HashTable()
        ht.insert("key1", "value1")
        assert ht.search("key1") == "value1"

    def test_insert_multiple(self):
        """Тест вставки нескольких элементов"""
        ht = HashTable()
        ht.insert("a", 1)
        ht.insert("b", 2)
        ht.insert("c", 3)

        assert ht.search("a") == 1
        assert ht.search("b") == 2
        assert ht.search("c") == 3
        assert len(ht) == 3

    def test_update_existing_key(self):
        """Тест обновления существующего ключа"""
        ht = HashTable()
        ht.insert("key", "old_value")
        result = ht.insert("key", "new_value")

        assert result is False  # Должен вернуть False при обновлении
        assert ht.search("key") == "new_value"
        assert len(ht) == 1  # Размер не должен измениться

    def test_search_nonexistent_key(self):
        """Тест поиска несуществующего ключа"""
        ht = HashTable()
        with pytest.raises(KeyError):
            ht.search("nonexistent")

    def test_delete(self):
        """Тест удаления элемента"""
        ht = HashTable()
        ht.insert("key", "value")
        deleted_value = ht.delete("key")

        assert deleted_value == "value"
        assert len(ht) == 0
        with pytest.raises(KeyError):
            ht.search("key")

    def test_delete_nonexistent_key(self):
        """Тест удаления несуществующего ключа"""
        ht = HashTable()
        with pytest.raises(KeyError):
            ht.delete("nonexistent")

    def test_delete_multiple(self):
        """Тест удаления нескольких элементов"""
        ht = HashTable()
        ht.insert("a", 1)
        ht.insert("b", 2)
        ht.insert("c", 3)

        ht.delete("b")
        assert len(ht) == 2
        assert ht.search("a") == 1
        assert ht.search("c") == 3
        with pytest.raises(KeyError):
            ht.search("b")


class TestHashTableDictInterface:
    """Тесты dict-подобного интерфейса"""

    def test_setitem_getitem(self):
        """Тест операторов [] для установки и получения значений"""
        ht = HashTable()
        ht["key"] = "value"
        assert ht["key"] == "value"

    def test_delitem(self):
        """Тест оператора del"""
        ht = HashTable()
        ht["key"] = "value"
        del ht["key"]

        assert len(ht) == 0
        with pytest.raises(KeyError):
            _ = ht["key"]

    def test_contains(self):
        """Тест оператора in"""
        ht = HashTable()
        ht["key"] = "value"

        assert "key" in ht
        assert "nonexistent" not in ht

    def test_len(self):
        """Тест функции len()"""
        ht = HashTable()
        assert len(ht) == 0

        ht["a"] = 1
        assert len(ht) == 1

        ht["b"] = 2
        ht["c"] = 3
        assert len(ht) == 3

        del ht["b"]
        assert len(ht) == 2


class TestHashTableMethods:
    """Тесты вспомогательных методов"""

    def test_contains_method(self):
        """Тест метода contains()"""
        ht = HashTable()
        ht.insert("key", "value")

        assert ht.contains("key") is True
        assert ht.contains("nonexistent") is False

    def test_get_method(self):
        """Тест метода get()"""
        ht = HashTable()
        ht.insert("key", "value")

        assert ht.get("key") == "value"
        assert ht.get("nonexistent") is None
        assert ht.get("nonexistent", "default") == "default"

    def test_keys(self):
        """Тест метода keys()"""
        ht = HashTable()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3

        keys = ht.keys()
        assert len(keys) == 3
        assert set(keys) == {"a", "b", "c"}

    def test_values(self):
        """Тест метода values()"""
        ht = HashTable()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3

        values = ht.values()
        assert len(values) == 3
        assert set(values) == {1, 2, 3}

    def test_items(self):
        """Тест метода items()"""
        ht = HashTable()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3

        items = ht.items()
        assert len(items) == 3
        assert set(items) == {("a", 1), ("b", 2), ("c", 3)}

    def test_clear(self):
        """Тест метода clear()"""
        ht = HashTable()
        ht["a"] = 1
        ht["b"] = 2
        ht["c"] = 3

        ht.clear()
        assert len(ht) == 0
        assert ht.keys() == []
        assert ht._capacity == HashTable.INITIAL_CAPACITY


class TestHashTableResize:
    """Тесты динамического изменения размера"""

    def test_resize_on_insert(self):
        """Тест увеличения размера при вставке"""
        ht = HashTable(capacity=4)
        initial_capacity = ht._capacity

        # заполняем таблицу до превышения load factor
        for i in range(10):
            ht[f"key_{i}"] = i

        # емкость должна увеличиться
        assert ht._capacity > initial_capacity
        assert len(ht) == 10

        # все элементы должны быть доступны
        for i in range(10):
            assert ht[f"key_{i}"] == i

    def test_resize_on_delete(self):
        """Тест уменьшения размера при удалении"""
        ht = HashTable()

        # добавляем много элементов
        for i in range(50):
            ht[f"key_{i}"] = i

        capacity_after_insert = ht._capacity

        # удаляем большую часть элементов
        for i in range(45):
            del ht[f"key_{i}"]

        # емкость должна уменьшиться
        assert ht._capacity < capacity_after_insert
        assert len(ht) == 5

        # оставшиеся элементы должны быть доступны
        for i in range(45, 50):
            assert ht[f"key_{i}"] == i

    def test_load_factor_maintained(self):
        """Тест поддержания load factor в допустимых пределах"""
        ht = HashTable()

        # добавляем элементы
        for i in range(100):
            ht[f"key_{i}"] = i
            stats = ht.get_stats()
            # Load factor не должен превышать максимум
            assert stats['load_factor'] <= HashTable.MAX_LOAD_FACTOR

    def test_no_shrink_below_threshold(self):
        """Тест, что таблица не уменьшается ниже минимального порога"""
        ht = HashTable()

        # добавляем и удаляем элементы
        for i in range(10):
            ht[f"key_{i}"] = i

        for i in range(9):
            del ht[f"key_{i}"]

        # емкость не должна быть меньше SHRINK_THRESHOLD
        assert ht._capacity >= HashTable.SHRINK_THRESHOLD


class TestHashTableCollisions:
    """Тесты обработки коллизий"""

    def test_collision_handling(self):
        """Тест обработки коллизий (разные ключи с одинаковым хешем)"""
        ht = HashTable(capacity=4)

        # создаем ключи, которые могут дать коллизии при малой емкости
        keys = [f"key_{i}" for i in range(20)]
        for i, key in enumerate(keys):
            ht[key] = i

        # все элементы должны быть доступны
        for i, key in enumerate(keys):
            assert ht[key] == i

        assert len(ht) == 20

    def test_collision_deletion(self):
        """Тест удаления при наличии коллизий"""
        ht = HashTable(capacity=4)

        for i in range(10):
            ht[f"key_{i}"] = i

        # удаляем некоторые элементы
        del ht["key_2"]
        del ht["key_5"]
        del ht["key_8"]

        # оставшиеся элементы должны быть доступны
        for i in [0, 1, 3, 4, 6, 7, 9]:
            assert ht[f"key_{i}"] == i

        assert len(ht) == 7


class TestHashTableKeyTypes:
    """Тесты с различными типами ключей"""

    def test_string_keys(self):
        """Тест со строковыми ключами"""
        ht = HashTable()
        ht["hello"] = "world"
        ht["foo"] = "bar"

        assert ht["hello"] == "world"
        assert ht["foo"] == "bar"

    def test_integer_keys(self):
        """Тест с целочисленными ключами"""
        ht = HashTable()
        ht[1] = "one"
        ht[2] = "two"
        ht[100] = "hundred"

        assert ht[1] == "one"
        assert ht[2] == "two"
        assert ht[100] == "hundred"

    def test_tuple_keys(self):
        """Тест с кортежами в качестве ключей"""
        ht = HashTable()
        ht[(1, 2)] = "tuple_value_1"
        ht[(3, 4, 5)] = "tuple_value_2"

        assert ht[(1, 2)] == "tuple_value_1"
        assert ht[(3, 4, 5)] == "tuple_value_2"

    def test_mixed_key_types(self):
        """Тест со смешанными типами ключей"""
        ht = HashTable()
        ht["string"] = 1
        ht[42] = 2
        ht[(1, 2)] = 3

        assert ht["string"] == 1
        assert ht[42] == 2
        assert ht[(1, 2)] == 3


class TestHashTableValueTypes:
    """Тесты с различными типами значений"""

    def test_different_value_types(self):
        """Тест с различными типами значений"""
        ht = HashTable()

        ht["int"] = 42
        ht["float"] = 3.14
        ht["string"] = "hello"
        ht["list"] = [1, 2, 3]
        ht["dict"] = {"a": 1}
        ht["none"] = None

        assert ht["int"] == 42
        assert ht["float"] == 3.14
        assert ht["string"] == "hello"
        assert ht["list"] == [1, 2, 3]
        assert ht["dict"] == {"a": 1}
        assert ht["none"] is None


class TestHashTableStats:
    """Тесты статистики таблицы"""

    def test_get_stats(self):
        """Тест метода get_stats()"""
        ht = HashTable()

        # Пустая таблица
        stats = ht.get_stats()
        assert stats['size'] == 0
        assert stats['load_factor'] == 0
        assert stats['max_chain_length'] == 0

        # Добавляем элементы
        for i in range(10):
            ht[f"key_{i}"] = i

        stats = ht.get_stats()
        assert stats['size'] == 10
        assert stats['capacity'] >= 10
        assert stats['load_factor'] > 0
        assert stats['max_chain_length'] >= 1

    def test_empty_table_stats(self):
        """Тест статистики пустой таблицы"""
        ht = HashTable()
        stats = ht.get_stats()

        assert stats['size'] == 0
        assert stats['load_factor'] == 0
        assert stats['non_empty_buckets'] == 0
        assert stats['max_chain_length'] == 0
        assert stats['collisions'] == 0


class TestHashTableEdgeCases:
    """Тесты граничных случаев"""

    def test_empty_table(self):
        """Тест пустой таблицы"""
        ht = HashTable()

        assert len(ht) == 0
        assert ht.keys() == []
        assert ht.values() == []
        assert ht.items() == []

    def test_single_element(self):
        """Тест с одним элементом"""
        ht = HashTable()
        ht["only"] = "one"

        assert len(ht) == 1
        assert ht["only"] == "one"

        del ht["only"]
        assert len(ht) == 0

    def test_large_number_of_elements(self):
        """Тест с большим количеством элементов"""
        ht = HashTable()
        n = 1000

        for i in range(n):
            ht[f"key_{i}"] = i

        assert len(ht) == n

        for i in range(n):
            assert ht[f"key_{i}"] == i

        for i in range(0, n, 2):
            del ht[f"key_{i}"]

        assert len(ht) == n // 2

    def test_repr(self):
        """Тест строкового представления"""
        ht = HashTable()
        ht["a"] = 1
        ht["b"] = 2

        repr_str = repr(ht)
        assert "HashTable" in repr_str
        assert "a" in repr_str or "b" in repr_str

    def test_duplicate_values(self):
        """Тест с дублирующимися значениями"""
        ht = HashTable()
        ht["key1"] = "same_value"
        ht["key2"] = "same_value"
        ht["key3"] = "same_value"

        assert len(ht) == 3
        assert ht["key1"] == "same_value"
        assert ht["key2"] == "same_value"
        assert ht["key3"] == "same_value"
