class Solution:
    from typing import List
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum = current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        max_sum = max(max_sum, current_sum)
        return max_sum

# Runtime 3 ms, 11.15 %
# Memory 17.74 mb, 44.25 %
def main():
    solution = Solution()
    nums1 = [10,20,30,5,10,50]
    nums2 = [10,20,30,40,50]
    nums3 = [12,17,15,13,10,11,12]
    print(solution.maxAscendingSum(nums=nums1))
    print(solution.maxAscendingSum(nums=nums2))
    print(solution.maxAscendingSum(nums=nums3))

if __name__ == '__main__':
    main()
