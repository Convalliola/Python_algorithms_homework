"""
Реализовать поиск подстроки в строке с помощью алгоритма Кнута — Морриса — Пратта
"""


def compute_prefix_function(pattern: str) -> list[int]:
    """
    Вычисляет префикс-функцию (failure function) для паттерна.

    pi[i] = длина наибольшего собственного префикса pattern[:i+1],
    который также является суффиксом этой подстроки.
    """
    m = len(pattern)
    pi = [0] * m

    k = 0  # длина текущего совпадающего префикса
    for i in range(1, m):
        # Откатываемся, пока не найдём совпадение или не дойдём до начала
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k - 1]

        if pattern[k] == pattern[i]:
            k += 1

        pi[i] = k

    return pi


def kmp_search(text: str, pattern: str) -> list[int]:
    """
    Поиск всех вхождений подстроки pattern в строке text
    с помощью алгоритма Кнута-Морриса-Пратта.

    Возвращает список индексов начала всех вхождений.
    """
    if not pattern or not text or len(pattern) > len(text):
        return []

    result = []
    n = len(text)
    m = len(pattern)

    # Вычисляем префикс-функцию
    pi = compute_prefix_function(pattern)

    k = 0  # количество совпавших символов паттерна
    for i in range(n):
        # откатываемся при несовпадении
        while k > 0 and pattern[k] != text[i]:
            k = pi[k - 1]

        if pattern[k] == text[i]:
            k += 1

        # полное совпадение
        if k == m:
            result.append(i - m + 1)
            k = pi[k - 1]  # продолжаем поиск перекрывающихся вхождений

    return result
