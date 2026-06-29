class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        current_len = len(nums)
        while current_len > 1:
            for i in range(current_len - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            current_len -= 1
        
        return nums[0]
