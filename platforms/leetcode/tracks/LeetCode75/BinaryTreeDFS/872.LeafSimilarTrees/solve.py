class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Runtime 0 ms, 100 %
# Memory 17.72 mb, 50.89 %
class Solution:
    from typing import Optional
    def leafSimilar(self, root1: Optional[TreeNode],
        root2: Optional[TreeNode]) -> bool:
        # Создадим функцию для сбора листьев
        def getLeaves(root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
            getLeaves(root.left, leaves)
            getLeaves(root.right, leaves)

        leaves1, leaves2 = [], []
        getLeaves(root1, leaves1)
        getLeaves(root2, leaves2)
        return leaves1 == leaves2
