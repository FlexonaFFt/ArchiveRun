class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMin(self, node: TreeNode) -> TreeNode:
        """Находит узел с минимальным значением в поддереве."""
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """Удаляет узел с заданным ключом из BST и возвращает измененное дерево."""
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.findMin(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root
