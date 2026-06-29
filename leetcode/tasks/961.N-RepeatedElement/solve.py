class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        nu = set(nums)
        for num in nu:
            wow = nums.count(num)
            if wow == n:
                return num
