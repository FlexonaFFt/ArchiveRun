class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        counter, n = 0, len(nums)
        nums.sort()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] > nums[k]: 
                        counter += 1
        return counter
        
# TL 224 / 241
# O (n ^ 3)