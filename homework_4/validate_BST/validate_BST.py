"""
На вход приходит root бинарного дерева.
Необходимо проверить, является ли это дерево бинарным деревом поиска.
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_BST(root):
    def validate(node, low=None, high=None):
        if node is None:
            return True
        if (low is not None and node.val <= low) or (high is not None and node.val >= high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root)

# итертивная версия, чтобы не упереться в RecursionError
def is_valid_BST_iterative(root):
    stack, cur, prev = [], root, None
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        if prev is not None and cur.val <= prev:
            return False
        prev = cur.val
        cur = cur.right
    return True