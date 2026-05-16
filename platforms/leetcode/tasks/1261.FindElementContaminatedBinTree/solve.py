class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Runtime 1 ms, 96.52 %
# Memory 22.37 mb, 10.70 %
from typing import Optional
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self._recover(root, 0)

    def _recover(self, node, value):
        if not node:
            return
        node.val = value
        self.values.add(value)
        self._recover(node.left, 2 * value + 1)
        self._recover(node.right, 2 * value + 2)

    def find(self, target):
        return target in self.values
