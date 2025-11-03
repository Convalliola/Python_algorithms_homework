"""
Дано бинарное дерево. Определить, является ли оно сбалансированным по высоте.
Сбалансированное по высоте бинарное дерево — это бинарное дерево, в котором глубина двух поддеревьев каждого узла никогда не отличается более чем на единицу.
Важно!
Тесты, в рамках которых необходимо рассмотреть как можно больше краевых кейсов.
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root):
    """
    Временная сложность: O(n), n количество узлов
    Пространственная сложность: O(h), h высота дерева
    """

    def check_height(node):
        """
        возвоащает высоту поддерева или -1 если дерево не сбалансировано
        """
        # пустой узел имеет высоту 0
        if node is None:
            return 0

        # проверяем левое поддерево
        left_height = check_height(node.left)
        if left_height == -1:
            return -1  # левое поддерево не сбалансировано

        # проверяем правое поддерево
        right_height = check_height(node.right)
        if right_height == -1:
            return -1  # правое поддерево не сбалансировано

        # проверяем разницу высот текущего узла
        if abs(left_height - right_height) > 1:
            return -1  # текущий узел не сбалансирован

        
        return max(left_height, right_height) + 1

    return check_height(root) != -1