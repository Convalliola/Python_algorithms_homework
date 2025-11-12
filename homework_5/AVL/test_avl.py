"""
Тесты для AVLTree
"""

import unittest
import sys
import os

# путь к модулю
sys.path.insert(0, os.path.dirname(__file__))
from avl import AVLTree, AVLNode


class TestAVLTree(unittest.TestCase):
    # базовые тесты

    def setUp(self):
        """Создание нового дерева перед каждым тестом"""
        self.avl = AVLTree()

    def test_empty_tree(self):
        """пустое дерево"""
        self.assertIsNone(self.avl.root)
        self.assertEqual(self.avl.inorder_traversal(), [])
        self.assertTrue(self.avl.is_balanced())

    def test_single_insert(self):
        """вставка одного элемента"""
        self.avl.insert(10)
        self.assertEqual(self.avl.root.key, 10)
        self.assertEqual(self.avl.inorder_traversal(), [10])
        self.assertTrue(self.avl.is_balanced())

    def test_multiple_inserts(self):
        """ вставка нескольких элементов"""
        elements = [10, 20, 30, 40, 50, 25]
        for elem in elements:
            self.avl.insert(elem)

        self.assertEqual(self.avl.inorder_traversal(), [10, 20, 25, 30, 40, 50])
        self.assertTrue(self.avl.is_balanced())

    def test_duplicate_insert(self):
        """ вставка дубликата (не должен добавляться)"""
        self.avl.insert(10)
        self.avl.insert(10)
        self.assertEqual(self.avl.inorder_traversal(), [10])

    def test_search_existing(self):
        """поиск существующего элемента"""
        elements = [10, 20, 30]
        for elem in elements:
            self.avl.insert(elem)

        self.assertTrue(self.avl.search(10))
        self.assertTrue(self.avl.search(20))
        self.assertTrue(self.avl.search(30))

    def test_search_non_existing(self):
        """поиск несуществующего элемента"""
        self.avl.insert(10)
        self.assertFalse(self.avl.search(20))

    def test_search_empty_tree(self):
        """поиск в пустом дереве"""
        self.assertFalse(self.avl.search(10))

    def test_delete_leaf(self):
        """удаление листа"""
        self.avl.insert(10)
        self.avl.insert(5)
        self.avl.insert(15)
        self.avl.delete(5)

        self.assertEqual(self.avl.inorder_traversal(), [10, 15])
        self.assertTrue(self.avl.is_balanced())

    def test_delete_node_with_one_child(self):
        """ удаление узла с одним потомком"""
        self.avl.insert(10)
        self.avl.insert(5)
        self.avl.insert(15)
        self.avl.insert(20)
        self.avl.delete(15)

        self.assertIn(20, self.avl.inorder_traversal())
        self.assertTrue(self.avl.is_balanced())

    def test_delete_node_with_two_children(self):
        """удаление узла с двумя потомками"""
        elements = [10, 5, 15, 3, 7, 12, 20]
        for elem in elements:
            self.avl.insert(elem)

        self.avl.delete(10)
        result = self.avl.inorder_traversal()

        self.assertNotIn(10, result)
        self.assertEqual(len(result), 6)
        self.assertTrue(self.avl.is_balanced())

    def test_delete_root(self):
        """удаления корня"""
        self.avl.insert(10)
        self.avl.delete(10)

        self.assertIsNone(self.avl.root)
        self.assertEqual(self.avl.inorder_traversal(), [])

    def test_delete_non_existing(self):
        """удаление несуществующего элемента"""
        self.avl.insert(10)
        self.avl.delete(20)

        self.assertEqual(self.avl.inorder_traversal(), [10])


class TestAVLBalancing(unittest.TestCase):
    """ проверка балансировки"""

    def setUp(self):
        self.avl = AVLTree()

    def test_left_left_rotation(self):
        """Left-Left случай (правый поворот)"""
        # Вставка в порядке, требующем правого поворота
        self.avl.insert(30)
        self.avl.insert(20)
        self.avl.insert(10)

        self.assertTrue(self.avl.is_balanced())
        self.assertEqual(self.avl.root.key, 20)
        self.assertEqual(self.avl.inorder_traversal(), [10, 20, 30])

    def test_right_right_rotation(self):
        """ Right-Right случай (левый поворот)"""
        # Вставка в порядке, требующем левого поворота
        self.avl.insert(10)
        self.avl.insert(20)
        self.avl.insert(30)

        self.assertTrue(self.avl.is_balanced())
        self.assertEqual(self.avl.root.key, 20)
        self.assertEqual(self.avl.inorder_traversal(), [10, 20, 30])

    def test_left_right_rotation(self):
        """ Left-Right случай"""
        self.avl.insert(30)
        self.avl.insert(10)
        self.avl.insert(20)

        self.assertTrue(self.avl.is_balanced())
        self.assertEqual(self.avl.root.key, 20)
        self.assertEqual(self.avl.inorder_traversal(), [10, 20, 30])

    def test_right_left_rotation(self):
        """ Right-Left случай"""
        self.avl.insert(10)
        self.avl.insert(30)
        self.avl.insert(20)

        self.assertTrue(self.avl.is_balanced())
        self.assertEqual(self.avl.root.key, 20)
        self.assertEqual(self.avl.inorder_traversal(), [10, 20, 30])

    def test_complex_balancing(self):
        """сложная балансировка с множественными вставками"""
        elements = [10, 20, 30, 40, 50, 25, 5, 15, 35]
        for elem in elements:
            self.avl.insert(elem)
            self.assertTrue(self.avl.is_balanced(),
                          f"Дерево не сбалансировано после вставки {elem}")

        self.assertEqual(sorted(elements), self.avl.inorder_traversal())

    def test_balancing_after_delete(self):
        """балансировка после удаления"""
        elements = [10, 20, 30, 40, 50, 25]
        for elem in elements:
            self.avl.insert(elem)

        self.avl.delete(10)
        self.assertTrue(self.avl.is_balanced())

        self.avl.delete(25)
        self.assertTrue(self.avl.is_balanced())


class TestAVLTraversal(unittest.TestCase):
    """Тесты для обходов дерева"""

    def setUp(self):
        """Создание нового дерева перед каждым тестом"""
        self.avl = AVLTree()

    def test_inorder_traversal(self):
        """Тест inorder обхода (должен вернуть отсортированный список)"""
        elements = [30, 10, 50, 20, 40]
        for elem in elements:
            self.avl.insert(elem)

        self.assertEqual(self.avl.inorder_traversal(), [10, 20, 30, 40, 50])

    def test_preorder_traversal(self):
        """Тест preorder обхода"""
        elements = [30, 10, 50, 20, 40]
        for elem in elements:
            self.avl.insert(elem)

        preorder = self.avl.preorder_traversal()
        # Первый элемент должен быть корнем
        self.assertEqual(preorder[0], self.avl.root.key)
        # Все элементы должны присутствовать
        self.assertEqual(sorted(preorder), [10, 20, 30, 40, 50])


class TestAVLHeight(unittest.TestCase):
    """Тесты для проверки высоты дерева"""

    def setUp(self):
        """Создание нового дерева перед каждым тестом"""
        self.avl = AVLTree()

    def test_empty_tree_height(self):
        """Тест высоты пустого дерева"""
        self.assertEqual(self.avl.get_height(self.avl.root), 0)

    def test_single_node_height(self):
        """Тест высоты дерева с одним узлом"""
        self.avl.insert(10)
        self.assertEqual(self.avl.get_height(self.avl.root), 1)

    def test_height_after_inserts(self):
        """Тест высоты после вставок"""
        elements = [10, 20, 30, 40, 50, 25]
        for elem in elements:
            self.avl.insert(elem)

        # Проверяем, что высота логарифмическая
        height = self.avl.get_height(self.avl.root)
        import math
        max_height = math.ceil(1.44 * math.log2(len(elements) + 2))
        self.assertLessEqual(height, max_height)


class TestAVLEdgeCases(unittest.TestCase):
    """Тесты для граничных случаев"""

    def setUp(self):
        """Создание нового дерева перед каждым тестом"""
        self.avl = AVLTree()

    def test_ascending_sequence(self):
        """Тест вставки элементов в возрастающем порядке"""
        elements = list(range(1, 11))
        for elem in elements:
            self.avl.insert(elem)

        self.assertTrue(self.avl.is_balanced())
        self.assertEqual(self.avl.inorder_traversal(), elements)

    def test_descending_sequence(self):
        """Тест вставки элементов в убывающем порядке"""
        elements = list(range(10, 0, -1))
        for elem in elements:
            self.avl.insert(elem)

        self.assertTrue(self.avl.is_balanced())
        self.assertEqual(self.avl.inorder_traversal(), list(range(1, 11)))

    def test_negative_numbers(self):
        """Тест с отрицательными числами"""
        elements = [-10, -5, 0, 5, 10]
        for elem in elements:
            self.avl.insert(elem)

        self.assertTrue(self.avl.is_balanced())
        self.assertEqual(self.avl.inorder_traversal(), elements)

    def test_large_tree(self):
        """Тест с большим количеством элементов"""
        elements = list(range(100))
        for elem in elements:
            self.avl.insert(elem)

        self.assertTrue(self.avl.is_balanced())
        self.assertEqual(len(self.avl.inorder_traversal()), 100)

    def test_insert_delete_sequence(self):
        """Тест последовательности вставок и удалений"""
        # Вставляем
        for i in range(1, 11):
            self.avl.insert(i)

        # Удаляем каждый второй
        for i in range(2, 11, 2):
            self.avl.delete(i)

        self.assertTrue(self.avl.is_balanced())
        self.assertEqual(self.avl.inorder_traversal(), [1, 3, 5, 7, 9])


class TestAVLBalance(unittest.TestCase):
    """Тесты баланс-фактора"""

    def setUp(self):
        """Создание нового дерева перед каждым тестом"""
        self.avl = AVLTree()

    def test_balance_factor(self):
        """Тест баланс-фактора узлов"""
        elements = [10, 20, 30, 40, 50, 25]
        for elem in elements:
            self.avl.insert(elem)

        # Проверяем, что баланс-фактор всех узлов в пределах [-1, 1]
        def check_balance(node):
            if not node:
                return True
            balance = self.avl.get_balance(node)
            if abs(balance) > 1:
                return False
            return check_balance(node.left) and check_balance(node.right)

        self.assertTrue(check_balance(self.avl.root))


if __name__ == '__main__':
    unittest.main(verbosity=2)
