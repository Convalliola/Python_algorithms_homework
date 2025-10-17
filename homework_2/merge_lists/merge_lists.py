"""
Задача: 
Даны два отсортированных односвязных списка list1 и list2

Необходимо объединить их в один новый отсортированный список.
Новый список должен быть составлен слиянием узлов двух исходных списков. 
Вернуть необходимо голову объединенного списка.
"""


class ListNode:
    """Узел односвязного списка"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists_with_dummy(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """
    Способ 1: Слияние с использованием фиктивного (dummy) узла.

    Алгоритм:
    1. Создаем dummy узел, который будет предшествовать голове результата
    2. Используем указатель current для построения нового списка
    3. Сравниваем элементы из list1 и list2, добавляя меньший к результату
    4. Когда один из списков закончится, присоединяем остаток другого
    5. Возвращаем dummy.next (голову результирующего списка)

    Временная сложность: O(n + m), где n и m - длины списков
    Пространственная сложность: O(1) - создаем только указатели, не новые узлы
    """
    dummy = ListNode(0)
    current = dummy  

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2

    return dummy.next


def merge_two_lists_without_dummy(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """
    Способ 2: Слияние без использования фиктивного узла.

    Алгоритм:
    1. Обрабатываем случаи, когда один из списков пуст
    2. Определяем голову результата (меньший из первых элементов)
    3. Используем указатель current для построения списка
    4. Сравниваем элементы и добавляем меньший к результату
    5. Присоединяем остаток непустого списка

    Временная сложность: O(n + m), где n и m - длины списков
    Пространственная сложность: O(1) - создаем только указатели
    """
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    current = head

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2

    return head


def create_linked_list(values: list[int]) -> ListNode | None:
    """
    Доп функция для запуска тестов: создает связный список из массива значений.
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head: ListNode | None) -> list[int]:
    """
    Доп функция, возвращающая список значений из связного списка.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
