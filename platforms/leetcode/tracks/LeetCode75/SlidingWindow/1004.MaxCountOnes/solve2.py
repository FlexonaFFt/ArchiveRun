class Solution:
    from typing import List
    def longestOnes(self, nums: List[int], k: int) -> int:
        flips, current_ones, max_ones, left = 0, 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                flips += 1
            current_ones += 1

            while flips > k:
                if nums[left] == 0:
                    flips -= 1
                current_ones -= 1
                left += 1
            max_ones = max(max_ones, current_ones)
        return max_ones


def main():
    solution = Solution()
    nums, k = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 10
    print(solution.longestOnes(nums, k))

if __name__ == '__main__':
    main()
