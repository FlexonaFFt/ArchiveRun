class Solution:
    from typing import List
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, total_sum = 0, sum(nums)
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1

# Runtime 8 ms, 42.12 %
# Memory 18.65 mb, 36.64 %
def main():
    nums1 = [1,7,3,6,5,6]
    nums2 = [1,2,3]
    nums3 = [2,1,-1]
    solution = Solution()
    print(solution.pivotIndex(nums1))
    print(solution.pivotIndex(nums2))
    print(solution.pivotIndex(nums3))

if __name__ == '__main__':
    main()
