class Solution:
    from typing import List
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, current_zeros, max_ones = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                current_zeros += 1
            while current_zeros > k:
                if nums[left] == 0:
                    current_zeros -= 1
                left += 1
            max_ones = max(max_ones, right - left + 1)
        return max_ones


def main():
    solution = Solution()
    nums, k = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 10
    print(solution.longestOnes(nums, k))

if __name__ == '__main__':
    main()
