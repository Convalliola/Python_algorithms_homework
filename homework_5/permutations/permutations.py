"""
На вход дан массив. Необходимо вернуть все возможные перестановки.

Вход: nums = [1,2,3]
Выход: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Вход: nums = [0,1]
Выход: [[0,1],[1,0]]
Вход: nums = [1]
Выход: [[1]]
Обязательно: в реализации предусмотреть визуализацию стека вызовов, в идеале использовать декоратор из первой задачи.
"""

import sys
import os

# путь к модулю tracer
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tracer'))
from tracer import tracer


def permute(nums, trace=False):
    """
    генерирует все возможные перестановки массива nums.
    На вход: список чисел и trace - если True, выводит трассировку рекурсивных вызовов
    возвращает:список всех перестановок
    """
    result = []

    if trace:
        # версия с трассировкой
        @tracer
        def backtrack(current, remaining):
            """
            Рекурсивная функция для генерации перестановок.
            current - текущая перестановка 
            remaining - оставшиеся элементы для добавления 
            """
            #  если нет оставшихся элементов
            if not remaining:
                result.append(current[:])  # копия текущей перестановки
                return

            # рекурсивный случай, перебираем все оставшиеся элементы
            for i in range(len(remaining)):
                element = remaining[i]
                # добавляем элемент к текущей перестановке
                current.append(element)
                # рекурсивно обрабатываем оставшиеся элементы
                new_remaining = remaining[:i] + remaining[i+1:]
                backtrack(current, new_remaining)
                # backtracking
                current.pop()
    else:
        # Версия без трассировки
        def backtrack(current, remaining):
            # нет оставшихся элементов
            if not remaining:
                result.append(current[:])  
                return

            # рекурсивный случай 
            for i in range(len(remaining)):
                element = remaining[i]
                current.append(element)
                new_remaining = remaining[:i] + remaining[i+1:]
                backtrack(current, new_remaining)
                current.pop()

    backtrack([], nums)
    return result


# пример использования
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [0, 1],
        [1]
    ]


    for nums in test_cases:
        print("\n")
        print(f"Входной массив: {nums}")
        print("\n")
        result = permute(nums, trace=True)
        print(f"\nВсего перестановок: {len(result)}")
        print(f"Результат: {result}")

    # примеры без трассировки 
    print("\n\n")
    print("РЕЗУЛЬТАТ БЕЗ ТРАССИРОВКИ")
    print("\n")

    for nums in test_cases:
        result = permute(nums, trace=False)
        print(f"\nВход: {nums}")
        print(f"Выход: {result}")
        print(f"Количество перестановок: {len(result)}")