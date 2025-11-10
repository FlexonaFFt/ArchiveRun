class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter, stack = 0, []
        for num in nums:
            if num == 0:
                stack.clear()
                continue

            while stack and stack[-1] > num:
                stack.pop()
            if not stack or stack[-1] < num:
                counter += 1
                stack.append(num)
        return counter
