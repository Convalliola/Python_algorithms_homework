from typing import List
"""
Задача: 
Даны 2 последовательности pushed и popped, содержащие уникальные целые числа. popped  является перестановкой pushed, 
то есть, все элементы совпадают, но может отличаться порядок.
Программа должна вернуть True, если эти последовательности могут получиться в результате некоторой последовательности операций push и pop на пустом стеке.
"""

def validate_stack_sequences(pushed: List[int], popped: List[int]) -> bool:
    """Возвращает True, если последовательности pushed и popped
    могут быть получены с помощью операций push/pop на пустом стеке.

    Алгоритм: симулируем стек. Проходим по pushed, кладём элементы в стек,
    и каждый раз, когда верх стека равен текущему ожидаемому элементу из popped,
    выполняем pop и двигаем указатель по popped.

    Временная сложность: O(n)
    Память: O(n)
    """
    if len(pushed) != len(popped):
        return False

    stack: List[int] = []
    pop_index = 0

    for value in pushed:
        stack.append(value)
        while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
            stack.pop()
            pop_index += 1

    return pop_index == len(popped)


if __name__ == "__main__":
    pass