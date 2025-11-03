"""
Тесты для проверки функции is_balanced.
"""

from balanced_binary_tree import TreeNode, is_balanced


def test_balanced_binary_tree():


    # пустое дерево
    print("Тест 1")
    root = None
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == True
    print("Пройден\n")

    # дерево с одним узлом
    print("Тест 2")
    root = TreeNode(1)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == True
    print("Пройден\n")

    # сбалансированное полное дерево
    print("Тест 3")
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == True
    print("Пройден\n")

    # несбалансированное дерево слева
    print("Тест 4:")
    #       1
    #      /
    #     2
    #    /
    #   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == False
    print("Пройден\n")

    # несбалансированное дерево справа
    print("Тест 5")
    #   1
    #    \
    #     2
    #      \
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == False
    print("Пройден\n")

    # сбалансированное с разницей высот 1
    print("Тест 6")
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == True
    print("Пройден\n")

    # несбалансированное дерево 
    print("Тест 7")
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    #  /
    # 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == False
    print("Пройден\n")

    # идеально сбалансированное дерево
    print("Тест 8")
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == True
    print("Пройден\n")

    # дерево с двумя узлами слева
    print("Тест 9")
    #   1
    #  /
    # 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == True
    print("Пройден\n")

    # дерево с двумя узлами справа
    print("Тест 10")
    # 1
    #  \
    #   2
    root = TreeNode(1)
    root.right = TreeNode(2)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == True
    print("Пройден\n")

    # сложное сбалансированное дерево
    print("Тест 11")
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    #    /
    #   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == True
    print("Пройден\n")

    # несбалансированное 
    print("Тест 12")
    #         1
    #        / \
    #       2   3
    #      /
    #     4
    #    /
    #   5
    #  /
    # 6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.left = TreeNode(6)
    result = is_balanced(root)
    print(f"Результат: {result}")
    assert result == False
    print("Пройден\n")

    print("\n")
    print("Все тесты пройдены!")
    print("\n")


if __name__ == "__main__":
    test_balanced_binary_tree()
