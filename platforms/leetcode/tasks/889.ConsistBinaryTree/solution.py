class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Runtime 0 ms, 100 %
# Memory 17.74 mb, 71.53 %
class Solution:
    from typing import Optional, List
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        left_root_val = preorder[1]
        left_root_idx = postorder.index(left_root_val)
        root.left = self.constructFromPrePost(preorder[1:left_root_idx+2], postorder[:left_root_idx+1])
        root.right = self.constructFromPrePost(preorder[left_root_idx+2:], postorder[left_root_idx+1:-1])
        return root
