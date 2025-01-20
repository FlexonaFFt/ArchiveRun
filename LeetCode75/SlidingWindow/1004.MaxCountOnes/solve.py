class Solution:
    from typing import List
    def longestOnes(self, nums: List[int], k: int) -> int:
        flips, current_ones, max_ones = 0, 0, 0
        for num in nums:
            if num == 0:
                flips += 1
            current_ones += 1
            if flips > k:
                current_ones = 0
                flips = 0
            else:
                max_ones = max(max_ones, current_ones)
        return max_ones


def main():
    solution = Solution()
    nums, k = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 10
    print(solution.longestOnes(nums, k))

if __name__ == '__main__':
    main()
