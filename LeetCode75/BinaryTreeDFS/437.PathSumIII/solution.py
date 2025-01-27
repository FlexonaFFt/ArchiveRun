class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
from collections import defaultdict
class Solution:
    from typing import Optional
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, currentSum):
            if not node:
                return 0
            currentSum += node.val
            count = prefix_sums[currentSum - targetSum]
            count += dfs(node.left, currentSum)
            count += dfs(node.right, currentSum)
            prefix_sums[currentSum] -= 1
            return count

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        return dfs(root, 0)
'''

from collections import defaultdict
class Solution:
    def pathSum(self, root, targetSum):
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val
            # Проверяем, есть ли подпуть с суммой targetSum
            count = prefix_sums.get(current_sum - targetSum, 0)

            # Обновляем текущую сумму в префиксных суммах
            prefix_sums[current_sum] += 1

            # Рекурсивно обходим левое и правое поддеревья
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # Убираем текущую сумму из префиксных сумм (backtracking)
            prefix_sums[current_sum] -= 1

            return count

        # Используем словарь для хранения префиксных сумм
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Инициализируем нулевой суммой

        return dfs(root, 0)
