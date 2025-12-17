"""
Longest common subsequence
Даны две строки.
Найти самую длинную последовательность символов, которая встречается в заданном порядке в обеих строках.
Символы не обязательно должны идти подряд
"""


def lcs(s1: str, s2: str) -> str:
    """
    Находит наибольшую общую подпоследовательность двух строк.
    Использует динамическое программирование.

    Возвращает саму подпоследовательность (не только длину).
    """
    n = len(s1)
    m = len(s2)

    # dp[i][j] = длина LCS для s1[:i] и s2[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Заполняем таблицу
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                # если символы совпали, берем диагональ + 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # берем максимум из левой или верхней ячейки
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # восстанавление подпоследовательности
    result = []
    i, j = n, m

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            # символ входит в LCS
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            #  вверх
            i -= 1
        else:
            #  влево
            j -= 1

    return "".join(reversed(result))


def lcs_length(s1: str, s2: str) -> int:
    """Возвращает только длину LCS."""
    n = len(s1)
    m = len(s2)

    # Оптимизация памяти, храним только две строки
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev

    return prev[m]


if __name__ == "__main__":
    string_1 = "AGGTAB"
    string_2 = "GXTXAYB"

    result = lcs(string_1, string_2)
    print(f"Строка 1: {string_1}")
    print(f"Строка 2: {string_2}")
    print(f"LCS: {result}")
    print(f"Длина: {len(result)}")

