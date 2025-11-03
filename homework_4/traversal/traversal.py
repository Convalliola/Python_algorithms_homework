"""
Реализовать все обходы дерева:
pre-order, post-order, in-order, reverse pre-order, reverse post-order, reverse in-order
Реализовать класс BST
В классе BST необходимо поддержать вставку для удобства тестирования
"""


class TreeNode:
    #узел бинарного дерева

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    #бинарное дерево поиска с поддержкой вставки

    def __init__(self):
        self.root = None

    def insert(self, val):
        
        #вставка значения в BST.
        #временная сложность O(h), h - высота дерева
        
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        #рекурсивная вставка
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def insert_list(self, values):
        #вставка списка значений
        for val in values:
            self.insert(val)


# Обходы дерева 

def preorder_traversal(root):
    #Pre-order: корень -> левое -> правое
    #Временная сложность: O(n)
    #Пространственная сложность: O(h) для рекурсии
    
    result = []

    def traverse(node):
        if node is None:
            return
        result.append(node.val)  # сначала корень
        traverse(node.left)       # затем левое поддерево
        traverse(node.right)      # потом правое поддерево

    traverse(root)
    return result


def inorder_traversal(root):

    #In-order: левое -> корень -> правое
    #для BST даёт отсортированную последовательность


    result = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)       
        result.append(node.val)  
        traverse(node.right)      

    traverse(root)
    return result


def postorder_traversal(root):
    #Post-order: левое -> правое -> корень

    result = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)       
        traverse(node.right)      
        result.append(node.val)  

    traverse(root)
    return result


def reverse_preorder_traversal(root):
    
    # Reverse pre-order  корень -> правое -> левое
    # Зеркальная версия pre-order
    # Временная сложность O(n), пространственная сложность O(h) для рекурсии
    
    result = []

    def traverse(node):
        if node is None:
            return
        result.append(node.val)   
        traverse(node.right)      
        traverse(node.left)       

    traverse(root)
    return result


def reverse_inorder_traversal(root):
    
    # Reverse in-order правое -> корень -> левое
    # Для BST даёт обратно отсортированную последовательность

    
    result = []

    def traverse(node):
        if node is None:
            return
        traverse(node.right)      
        result.append(node.val) 
        traverse(node.left)      

    traverse(root)
    return result


def reverse_postorder_traversal(root):
    
    # Reverse post-order: правое -> левое -> корень
    # Зеркальная версия post-order

    
    result = []

    def traverse(node):
        if node is None:
            return
        traverse(node.right)      
        traverse(node.left)      
        result.append(node.val)  

    traverse(root)
    return result


# итеративные версии 

def preorder_iterative(root):
    
    #итеративная версия pre-order обхода.

    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # добавляем правый, затем левый (чтобы левый обработался первым)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def inorder_iterative(root):
    
    #итеративная версия in-order 
    
    result = []
    stack = []
    current = root

    while stack or current:
        # Идём влево до конца
        while current:
            stack.append(current)
            current = current.left

        # Обрабатываем узел
        current = stack.pop()
        result.append(current.val)

        # Переходим к правому поддереву
        current = current.right

    return result


def postorder_iterative(root):
    
    #итеративная версия post-order обхода.
    #использует два стека.
    
    if root is None:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    result = []
    while stack2:
        result.append(stack2.pop().val)

    return result
