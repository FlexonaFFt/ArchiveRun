class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left= left
        self.right = right


class Solution:
    from typing import Optional
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack, i, n = [], 0, len(traversal)
        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1

            node = TreeNode(value)
            if depth == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                while depth < len(stack):
                    stack.pop()
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None
