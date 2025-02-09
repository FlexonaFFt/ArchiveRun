class Solution:
    from typing import List
    def countBadPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        diffCounter = defaultdict(int)
        badPairs = 0

        for i in range(len(nums)):
            diff = i - nums[i]
            badPairs += i - diffCounter[diff]
            diffCounter[diff] += 1
        return badPairs

# Runtime 103 ms, 62 %
# Memory 38.81 mb, 59.29 %
def main():
    solution = Solution()
    print(solution.countBadPairs([4,1,3,3]))
    print(solution.countBadPairs([1,2,3,4,5]))

if __name__ == '__main__':
    main()
