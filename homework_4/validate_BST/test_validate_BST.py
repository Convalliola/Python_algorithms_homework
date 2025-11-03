"""
Расширенные тесты для is_valid_BST.
"""

from validate_BST import TreeNode, is_valid_BST, is_valid_BST_iterative


def test_basic_cases():
    """Базовые тесты для обеих версий."""
    print("Базовые тесты\n")

    # Пустое дерево
    print("Тест 1")
    root = None
    assert is_valid_BST(root) == True
    assert is_valid_BST_iterative(root) == True
    print("Пройден\n")

    # Один узел
    print("Тест 2")
    root = TreeNode(5)
    assert is_valid_BST(root) == True
    assert is_valid_BST_iterative(root) == True
    print("Пройден\n")

    # Валидное BST
    print("Тест 3")
    #       5
    #      / \
    #     3   7
    #    / \
    #   2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    assert is_valid_BST(root) == True
    assert is_valid_BST_iterative(root) == True
    print("Пройден\n")

    # Невалидное BST
    print("Тест 4")
    #     5
    #    / \
    #   7   3
    root = TreeNode(5)
    root.left = TreeNode(7)
    root.right = TreeNode(3)
    assert is_valid_BST(root) == False
    assert is_valid_BST_iterative(root) == False
    print("Пройден\n")


def test_none_boundaries():
    """Тесты для None границ """
    print("\n")
    # отрицательные числа
    print("Тест 9: Отрицательные числа")
    #       0
    #      / \
    #   -10  10
    #    /     \
    #  -20     20
    root = TreeNode(0)
    root.left = TreeNode(-10)
    root.right = TreeNode(10)
    root.left.left = TreeNode(-20)
    root.right.right = TreeNode(20)
    assert is_valid_BST(root) == True
    assert is_valid_BST_iterative(root) == True
    print("Пройден\n")

    # смешанные int и float
    print("Тест 10: Большие числа")
    root = TreeNode(1000000)
    root.left = TreeNode(-1000000)
    root.right = TreeNode(2000000)
    assert is_valid_BST(root) == True
    assert is_valid_BST_iterative(root) == True
    print("Пройден\n")


def test_deep_tree():
    """Тест глубокого дерева для проверки RecursionError"""
    print("\n")

    print("Тест 11")
    #  глубокое дерево с перекосом вправо
    root = TreeNode(0)
    current = root
    for i in range(1, 1000):
        current.right = TreeNode(i)
        current = current.right

    # Рекурсивная версия может упасть на очень глубоких деревьях
    # но 1000 узлов обычно ещё ок
    try:
        assert is_valid_BST(root) == True
        print("Рекурсивная версия: ОК")
    except RecursionError:
        print("Рекурсивная версия: RecursionError (ожидаемо на глубоких деревьях)")

    # итеративная версия 
    assert is_valid_BST_iterative(root) == True
    print("Итеративная версия: ОК")
    print("Пройден\n")


def test_edge_cases():
    """Краевые случаи"""
    print("\n")

    # нарушение в глубине
    print("Тест 12")
    #       10
    #      /  \
    #     5    15
    #         /  \
    #        6   20  <- 6 < 10, нарушение!
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    assert is_valid_BST(root) == False
    assert is_valid_BST_iterative(root) == False
    print("Пройден\n")

    # Только левое поддерево
    print("Тест 14")
    #       10
    #      /
    #     5
    #    /
    #   3
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    assert is_valid_BST(root) == True
    assert is_valid_BST_iterative(root) == True
    print("Пройден\n")

    # Только правое поддерево
    print("Тест 15")
    #   5
    #    \
    #     7
    #      \
    #       9
    root = TreeNode(5)
    root.right = TreeNode(7)
    root.right.right = TreeNode(9)
    assert is_valid_BST(root) == True
    assert is_valid_BST_iterative(root) == True
    print("Пройден\n")


def run_all_tests():
    """Запуск всех тестов."""
    print("\n")

    test_basic_cases()
    test_none_boundaries()
    test_deep_tree()
    test_edge_cases()

    print("\n")
    print("Все тесты успешно пройдены!")
    print("\n")


if __name__ == "__main__":
    run_all_tests()
