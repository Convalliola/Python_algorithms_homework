"""
Реализуйте собственную хеш-таблицу — структуру данных, которая хранит пары «ключ–значение» и позволяет выполнять три операции:
 • вставка элемента,
 • поиск по ключу,
 • удаление элемента.
"""


class HashTable:
    """
    Хеш-таблица с открытой адресацией (методом цепочек).

    Особенности реализации:
    - Разрешение коллизий методом цепочек (chaining)
    - Динамическое изменение размера при достижении load factor
    - Поддержка любых hashable типов ключей
    - O(1) среднее время для insert, search, delete
    """

    # константы для управления размером таблицы
    INITIAL_CAPACITY = 16
    MAX_LOAD_FACTOR = 0.75  # порог для увеличения размера
    MIN_LOAD_FACTOR = 0.25  # порог для уменьшения размера
    SHRINK_THRESHOLD = 32   # минимальный размер для уменьшения

    def __init__(self, capacity=None):
        """
        Инициализация хеш-таблицы.

        Args:
            capacity: Начальная емкость таблицы (по умолчанию INITIAL_CAPACITY)
        """
        if capacity is None:
            # Используем максимум из INITIAL_CAPACITY и SHRINK_THRESHOLD
            self._capacity = max(self.INITIAL_CAPACITY, self.SHRINK_THRESHOLD)
        else:
            self._capacity = capacity
        self._size = 0
        # Используем список списков для хранения цепочек
        self._buckets = [[] for _ in range(self._capacity)]

    def _hash(self, key):
        """
        Хеш-функция для вычисления индекса bucket'а.
        На вход: ключ для хеширования
        Возвращает: индекс bucketа в диапазоне [0, capacity)
        """
        # используем встроенную функцию hash() и берем остаток от деления
        return hash(key) % self._capacity

    def _resize(self, new_capacity):
        """
        Изменяет размер таблицы и перехеширует все элементы.

        На вход: new_capacity - новая емкость таблицы
        """
        # сохраняем старые данные
        old_buckets = self._buckets

        # создаем новую таблицу
        self._capacity = new_capacity
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

        # перехешируем все элементы напрямую, без вызова insert()
        # чтобы избежать бесконечной рекурсии через _check_resize()
        for bucket in old_buckets:
            for key, value in bucket:
                index = self._hash(key)
                self._buckets[index].append((key, value))
                self._size += 1

    def _check_resize(self):
        """
        Проверяет load factor и изменяет размер таблицы при необходимости.
        """
        load_factor = self._size / self._capacity

        # если load factor превышает максимум увеличиваем размер
        if load_factor > self.MAX_LOAD_FACTOR:
            self._resize(self._capacity * 2)

        # если load factor меньше минимума и текущая емкость больше порога,
        # уменьшаем размер, но не меньше чем SHRINK_THRESHOLD
        elif (load_factor < self.MIN_LOAD_FACTOR and
              self._capacity > self.SHRINK_THRESHOLD):
            new_capacity = self._capacity // 2
            # не уменьшаем меньше порога
            if new_capacity >= self.SHRINK_THRESHOLD:
                self._resize(new_capacity)

    def insert(self, key, value):
        """
        Вставляет пару ключ-значение в таблицу.
        Если ключ уже существует, обновляет значение.

        На вход:
            key -  ключ (должен быть hashable)
            value - значение
        Возвращает:
            bool - True, если элемент был добавлен; False, если обновлен
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        # проверяем, существует ли уже такой ключ
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # обновляем существующее значение
                bucket[i] = (key, value)
                return False

        # добавляем новую пару
        bucket.append((key, value))
        self._size += 1

        # проверяем необходимость изменения размера
        self._check_resize()

        return True

    def search(self, key):
        """
        Ищет значение по ключу.
        На вход: key - ключ для поиска
        Возращает: значение, соответствующее ключу
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        """
        Удаляет элемент по ключу.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1

                # проверяем необходимость уменьшения размера
                self._check_resize()

                return v

        raise KeyError(f"Key '{key}' not found")

    def contains(self, key):
        """
        Проверяет наличие ключа в таблице.
        На вход: key
        Возвращает: bool - True, если ключ существует; False иначе
        """
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def get(self, key, default=None):
        """
        Возвращает значение по ключу или значение по умолчанию.
        """
        try:
            return self.search(key)
        except KeyError:
            return default

    def keys(self):
        """
        Возвращает список всех ключей.
        """
        result = []
        for bucket in self._buckets:
            for key, _ in bucket:
                result.append(key)
        return result

    def values(self):
        """
        Возвращает список всех значений.
        """
        result = []
        for bucket in self._buckets:
            for _, value in bucket:
                result.append(value)
        return result

    def items(self):
        """
        Возвращает список всех пар (ключ, значение).
        """
        result = []
        for bucket in self._buckets:
            result.extend(bucket)
        return result

    def clear(self):
        """
        Очищает таблицу.
        """
        self._buckets = [[] for _ in range(self.INITIAL_CAPACITY)]
        self._capacity = self.INITIAL_CAPACITY
        self._size = 0

    def __len__(self):
        """
        Возвращает количество элементов в таблице.
        """
        return self._size

    def __contains__(self, key):
        """
        Поддержка оператора 'in'.
        """
        return self.contains(key)

    def __getitem__(self, key):
        """
        Поддержка синтаксиса table[key].
        """
        return self.search(key)

    def __setitem__(self, key, value):
        """
        Поддержка синтаксиса table[key] = value.
        """
        self.insert(key, value)

    def __delitem__(self, key):
        """
        Поддержка синтаксиса del table[key].
        """
        self.delete(key)

    def __repr__(self):
        """
        Строковое представление таблицы.
        """
        items = ', '.join(f'{k}: {v}' for k, v in self.items())
        return f'HashTable({{{items}}})'

    def get_stats(self):
        """
        Возвращает статистику таблицы для анализа производительности.
        """
        chain_lengths = [len(bucket) for bucket in self._buckets]
        non_empty_buckets = sum(1 for length in chain_lengths if length > 0)

        return {
            'size': self._size,
            'capacity': self._capacity,
            'load_factor': self._size / self._capacity if self._capacity > 0 else 0,
            'non_empty_buckets': non_empty_buckets,
            'max_chain_length': max(chain_lengths) if chain_lengths else 0,
            'avg_chain_length': sum(chain_lengths) / len(chain_lengths) if chain_lengths else 0,
            'collisions': sum(1 for length in chain_lengths if length > 1)
        }
