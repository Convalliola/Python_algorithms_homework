"""
Тесты для всех обходов дерева и класса BST.
"""

from traversal import (
    BST, TreeNode,
    preorder_traversal, inorder_traversal, postorder_traversal,
    reverse_preorder_traversal, reverse_inorder_traversal, reverse_postorder_traversal,
    preorder_iterative, inorder_iterative, postorder_iterative
)


def test_bst_insertion():

    print("Тест вставки\n")

    bst = BST()
    values = [5, 3, 7, 1, 4, 6, 9]

    bst.insert_list(values)

    # проверяем структуру через in-order (должен быть отсортирован)
    result = inorder_traversal(bst.root)
    expected = sorted(values)

    print(f"In-order обход: {result}")
    print(f"Ожидалось: {expected}")

    assert result == expected
    print("Тест пройден\n")


def test_standard_traversals():
    
    print("Тест стандартных обходов\n")

    bst = BST()
    bst.insert_list([5, 3, 7, 1, 4, 6, 9])
    root = bst.root

    # Pre-order: корень -> левое -> правое
    print("Pre-order (корень -> левое -> правое):")
    result = preorder_traversal(root)
    print(f"  Результат: {result}")
    assert result == [5, 3, 1, 4, 7, 6, 9]
    print("Корректно\n")

    # In-order: левое -> корень -> правое
    print("In-order (левое -> корень -> правое):")
    result = inorder_traversal(root)
    print(f"  Результат: {result}")
    assert result == [1, 3, 4, 5, 6, 7, 9]
    print("Корректно (отсортировано для BST)\n")

    # Post-order: левое -> правое -> корень
    print("Post-order (левое -> правое -> корень):")
    result = postorder_traversal(root)
    print(f"  Результат: {result}")
    assert result == [1, 4, 3, 6, 9, 7, 5]
    print("Корректно\n")


def test_reverse_traversals():
    print("Тест обратных обходов\n")

    # используем то же дерево
    bst = BST()
    bst.insert_list([5, 3, 7, 1, 4, 6, 9])
    root = bst.root

    # Reverse pre-order: корень -> правое -> левое
    print("Reverse pre-order (корень -> правое -> левое):")
    result = reverse_preorder_traversal(root)
    print(f"  Результат: {result}")
    assert result == [5, 7, 9, 6, 3, 4, 1]
    print("Корректно\n")

    # Reverse in-order: правое -> корень -> левое
    print("Reverse in-order (правое -> корень -> левое):")
    result = reverse_inorder_traversal(root)
    print(f"  Результат: {result}")
    assert result == [9, 7, 6, 5, 4, 3, 1]
    print("Корректно (обратная сортировка для BST)\n")

    # Reverse post-order: правое -> левое -> корень
    print("Reverse post-order (правое -> левое -> корень):")
    result = reverse_postorder_traversal(root)
    print(f"  Результат: {result}")
    assert result == [9, 6, 7, 4, 1, 3, 5]
    print(" Корректно\n")


def test_iterative_versions():
    
    print("Тест итеративных версий\n")

    bst = BST()
    bst.insert_list([5, 3, 7, 1, 4, 6, 9])
    root = bst.root

    print("Сравнение рекурсивных и итеративных версий:")

    rec_pre = preorder_traversal(root)
    iter_pre = preorder_iterative(root)
    print(f"  Pre-order: рекурсия={rec_pre}, итерация={iter_pre}")
    assert rec_pre == iter_pre
    print("Совпадают\n")

    rec_in = inorder_traversal(root)
    iter_in = inorder_iterative(root)
    print(f"  In-order: рекурсия={rec_in}, итерация={iter_in}")
    assert rec_in == iter_in
    print(" Совпадают\n")

    rec_post = postorder_traversal(root)
    iter_post = postorder_iterative(root)
    print(f"  Post-order: рекурсия={rec_post}, итерация={iter_post}")
    assert rec_post == iter_post
    print("Совпадают\n")


def test_edge_cases():

    print("Тест граничных случаев\n")

    # пустое дерево
    print("Тест 1")
    root = None
    assert preorder_traversal(root) == []
    assert inorder_traversal(root) == []
    assert postorder_traversal(root) == []
    print("Все обходы возвращают пустой список\n")

    # дерево с одним узлом
    print("Тест 2")
    root = TreeNode(42)
    assert preorder_traversal(root) == [42]
    assert inorder_traversal(root) == [42]
    assert postorder_traversal(root) == [42]
    assert reverse_preorder_traversal(root) == [42]
    assert reverse_inorder_traversal(root) == [42]
    assert reverse_postorder_traversal(root) == [42]
    print("Все обходы возвращают [42]\n")

    # дерево-цепочка (только левые дети)
    print("Тест 3")
    #     3
    #    /
    #   2
    #  /
    # 1
    bst = BST()
    bst.insert_list([3, 2, 1])
    root = bst.root

    pre = preorder_traversal(root)
    in_order = inorder_traversal(root)
    post = postorder_traversal(root)

    print(f"  Pre-order: {pre}")
    print(f"  In-order: {in_order}")
    print(f"  Post-order: {post}")

    assert pre == [3, 2, 1]
    assert in_order == [1, 2, 3]
    assert post == [1, 2, 3]
    print("Корректно\n")

    # только правые дети
    print("Тест 4")
    # 1
    #  \
    #   2
    #    \
    #     3
    bst = BST()
    bst.insert_list([1, 2, 3])
    root = bst.root

    pre = preorder_traversal(root)
    in_order = inorder_traversal(root)
    post = postorder_traversal(root)

    print(f"  Pre-order: {pre}")
    print(f"  In-order: {in_order}")
    print(f"  Post-order: {post}")

    assert pre == [1, 2, 3]
    assert in_order == [1, 2, 3]
    assert post == [3, 2, 1]
    print("Корректно\n")


def test_complex_tree():
   
    print("Тест сложного дерева\n")

    bst = BST()
    bst.insert_list([10, 5, 15, 3, 7, 12, 20, 1, 6, 13])
    root = bst.root

    # все обходы
    results = {
        "Pre-order": preorder_traversal(root),
        "In-order": inorder_traversal(root),
        "Post-order": postorder_traversal(root),
        "Reverse pre-order": reverse_preorder_traversal(root),
        "Reverse in-order": reverse_inorder_traversal(root),
        "Reverse post-order": reverse_postorder_traversal(root),
    }

    for name, result in results.items():
        print(f"{name:20}: {result}")

    assert results["In-order"] == [1, 3, 5, 6, 7, 10, 12, 13, 15, 20]
    assert results["Reverse in-order"] == [20, 15, 13, 12, 10, 7, 6, 5, 3, 1]

    print("\nВсе обходы корректны\n")


def run_all_tests():
    # запуск всех тестов
    print()

    test_bst_insertion()
    test_standard_traversals()
    test_reverse_traversals()
    test_iterative_versions()
    test_edge_cases()
    test_complex_tree()


    print("Все тесты пройдены\n")



if __name__ == "__main__":
    run_all_tests()
