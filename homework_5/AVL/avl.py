"""
Реализовать класс AVL, который будет представлять собой avl-дерево. Поддержать следующие операции:

* вставка
* удаление
* поиск
"""


class AVLNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def __init__(self):
        self.root = None

    def get_height(self, node):
        # высота узла
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        # разница высот левого и правого поддеревьев
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node):
       # Обновить высоту узла
        if not node:
            return
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_right(self, z):
        # правый поворот вокруг узла z
   
        y = z.left
        B = y.right

        # выполняем поворот
        y.right = z
        z.left = B

        # обновляем высоты
        self.update_height(z)
        self.update_height(y)

        return y

    def rotate_left(self, z):
        
        # Левый поворот вокруг узла z

        y = z.right
        B = y.left

        # Выполняем поворот
        y.left = z
        z.right = B

        # Обновляем высоты
        self.update_height(z)
        self.update_height(y)

        return y

    def insert(self, key):

        # Вставка ключа в AVL-дерево

        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """
        Рекурсивная вставка ключа
        """
        # Стандартная вставка в BST
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            # Дубликаты не допускаются
            return node

        # Обновляем высоту узла
        self.update_height(node)

        # Получаем баланс-фактор
        balance = self.get_balance(node)

        # Балансировка дерева (4 случая)

        # Left-Left случай
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Right-Right случай
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Left-Right случай
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right-Left случай
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def search(self, key):
        """
        Поиск ключа в дереве
        возвращает: True если ключ найден, False если нет
        """
        return self._search(self.root, key)

    def _search(self, node, key):
        """
        рекурсивный поиск ключа
        принимает на вход: текущий узел и значение для поиска
        возвращает: True если ключ найден, False если нет
        """
        if not node:
            return False

        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def get_min_value_node(self, node):
        # узел с минимальным значением в поддереве
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, key):
        # удаление ключа из дерева
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """
        Рекурсивное удаление ключа
        Принимает на вход: текущий узел и значение для удаления
        возвращает: корень поддерева после удаления и балансировки
        """
        # Стандартное удаление из BST
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел найден, удаляем его
            # узел с одним потомком или без потомков
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # узел с двумя потомками
            # Находим минимальный узел в правом поддереве 
            successor = self.get_min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        # если дерево имело только один узел
        if not node:
            return node

        # обновляем высоту узла
        self.update_height(node)

        # получаем баланс-фактор
        balance = self.get_balance(node)

        # Балансировка дерева 

        # Left-Left случай
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        # Left-Right случай
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right-Right случай
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        # Right-Left случай
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def inorder_traversal(self):
        """
        обход дерева в порядке возрастания (inorder)
        возвращает: список ключей в отсортированном порядке
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        # рекурсивный inorder обход
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def preorder_traversal(self):
        """
        preorder
        возвращает: список ключей в порядке preorder
        """
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        # рекурсивный preorder обход
        if node:
            result.append(node.key)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def is_balanced(self):
        
        # является ли дерево сбалансированным
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        # рекурсивная проверка балансировки
        if not node:
            return True

        balance = self.get_balance(node)
        if abs(balance) > 1:
            return False

        return self._is_balanced(node.left) and self._is_balanced(node.right)
