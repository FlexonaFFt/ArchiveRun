class TreeRoot: 
    
    def __init__(self, key: int, depth: int):
        self.key = key 
        self.depth = depth
        self.left = {}
        self.right = {}


class TreeNode:
    
    def __init__(self, key: int):
        self.key = key 
        self.left = {}
        self.right = {}


class Solution:

    def insert(self, tree, el: int, depth: int):
        if not tree: tree = TreeRoot(el, depth)
        else: 
            current_node, current_depth = tree, 0

            while True:
                current_depth += 1

                if el < current_node.key:
                    if current_node.left: 
                        current_node = current_node.left 
                    else: 
                        current_node.left = TreeNode(el) 
                        tree.depth = max(tree.depth, current_depth + 1)
                        break 

                else: 
                    if current_node.right:
                        current_node = current_node.right 
                    else: 
                        current_node.right = TreeNode(el)
                        tree.depth = max(tree.depth, current_depth + 1)
                        break 

        return tree 

    def func(self, nums) -> int: 
        tree = None 

        for i in nums: 
            i = int(i)
            if not i: break 

            tree = self.insert(tree, i, 1)
        return tree.depth

    def main(self) -> None:
        string = list(dict.fromkeys(input().split()))
        print(self.func(string))


if __name__ == '__main__':
    Solution().main()